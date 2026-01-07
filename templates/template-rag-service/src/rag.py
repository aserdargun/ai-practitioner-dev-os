"""RAG chain implementation."""

import logging
import os
from pathlib import Path

from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

logger = logging.getLogger(__name__)

# Default configuration
DEFAULT_PERSIST_DIR = "data/chroma_db"
DEFAULT_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


class RAGChain:
    """RAG chain for question answering."""

    def __init__(
        self,
        persist_dir: str | None = None,
        embedding_model: str | None = None,
    ):
        """Initialize RAG chain.

        Args:
            persist_dir: Directory for Chroma database
            embedding_model: Name of embedding model
        """
        self.persist_dir = persist_dir or os.getenv("CHROMA_PERSIST_DIR", DEFAULT_PERSIST_DIR)
        self.embedding_model = embedding_model or DEFAULT_MODEL_NAME

        self.embeddings = HuggingFaceEmbeddings(model_name=self.embedding_model)
        self.vectorstore = None
        self.retriever = None
        self.chain = None

        self._load_vectorstore()

    def _load_vectorstore(self) -> None:
        """Load existing vector store if available."""
        if Path(self.persist_dir).exists():
            try:
                self.vectorstore = Chroma(
                    persist_directory=self.persist_dir,
                    embedding_function=self.embeddings,
                )
                self.retriever = self.vectorstore.as_retriever(search_kwargs={"k": 4})
                logger.info(f"Loaded vector store from {self.persist_dir}")
            except Exception as e:
                logger.warning(f"Could not load vector store: {e}")

    def _format_docs(self, docs: list) -> str:
        """Format retrieved documents for context."""
        return "\n\n".join(doc.page_content for doc in docs)

    def _build_chain(self, llm):
        """Build the RAG chain.

        Args:
            llm: Language model to use
        """
        prompt = ChatPromptTemplate.from_template(
            """Answer the question based only on the following context:

Context:
{context}

Question: {question}

Answer the question directly and concisely. If the answer is not in the context,
say "I don't have enough information to answer this question."
"""
        )

        self.chain = (
            {"context": self.retriever | self._format_docs, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )

    def query(self, question: str, top_k: int = 4) -> dict:
        """Query the RAG system.

        Args:
            question: Question to answer
            top_k: Number of documents to retrieve

        Returns:
            Dict with answer and sources
        """
        if not self.retriever:
            return {
                "answer": "No documents have been indexed. Please index documents first.",
                "sources": [],
                "confidence": 0.0,
            }

        # Update retriever k value
        self.retriever.search_kwargs["k"] = top_k

        # Get relevant documents
        docs = self.retriever.get_relevant_documents(question)

        # If no chain (no LLM), return just the context
        if not self.chain:
            context = self._format_docs(docs)
            return {
                "answer": f"Retrieved context (no LLM configured):\n\n{context}",
                "sources": [doc.metadata.get("source", "unknown") for doc in docs],
                "confidence": 0.5,
            }

        # Run the chain
        answer = self.chain.invoke(question)

        return {
            "answer": answer,
            "sources": [doc.metadata.get("source", "unknown") for doc in docs],
            "confidence": 0.8,  # Placeholder
        }

    def set_llm(self, llm) -> None:
        """Set the language model and build chain.

        Args:
            llm: Language model instance
        """
        self._build_chain(llm)


# Global RAG chain instance
_rag_chain: RAGChain | None = None


def get_rag_chain() -> RAGChain:
    """Get or create RAG chain singleton."""
    global _rag_chain
    if _rag_chain is None:
        _rag_chain = RAGChain()
    return _rag_chain
