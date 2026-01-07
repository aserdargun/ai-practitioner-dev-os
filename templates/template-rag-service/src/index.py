"""Document indexing utilities."""

import argparse
import logging
from pathlib import Path

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_documents(docs_dir: str) -> list:
    """Load documents from a directory.

    Args:
        docs_dir: Path to documents directory

    Returns:
        List of loaded documents
    """
    logger.info(f"Loading documents from {docs_dir}")

    # Support multiple file types
    loaders = [
        DirectoryLoader(docs_dir, glob="**/*.txt", loader_cls=TextLoader),
        DirectoryLoader(docs_dir, glob="**/*.md", loader_cls=TextLoader),
    ]

    documents = []
    for loader in loaders:
        try:
            documents.extend(loader.load())
        except Exception as e:
            logger.warning(f"Error loading with {loader}: {e}")

    logger.info(f"Loaded {len(documents)} documents")
    return documents


def split_documents(
    documents: list,
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
) -> list:
    """Split documents into chunks.

    Args:
        documents: List of documents
        chunk_size: Size of each chunk
        chunk_overlap: Overlap between chunks

    Returns:
        List of document chunks
    """
    logger.info(f"Splitting documents (chunk_size={chunk_size}, overlap={chunk_overlap})")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )

    chunks = text_splitter.split_documents(documents)
    logger.info(f"Created {len(chunks)} chunks")
    return chunks


def create_vectorstore(
    chunks: list,
    persist_dir: str,
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2",
) -> Chroma:
    """Create and persist vector store.

    Args:
        chunks: Document chunks
        persist_dir: Directory to persist database
        embedding_model: Name of embedding model

    Returns:
        Chroma vector store
    """
    logger.info(f"Creating vector store at {persist_dir}")

    embeddings = HuggingFaceEmbeddings(model_name=embedding_model)

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_dir,
    )

    vectorstore.persist()
    logger.info("Vector store created and persisted")

    return vectorstore


def index_documents(
    docs_dir: str,
    persist_dir: str = "data/chroma_db",
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
) -> dict:
    """Index documents from directory.

    Args:
        docs_dir: Path to documents
        persist_dir: Path to persist vector store
        chunk_size: Chunk size for splitting
        chunk_overlap: Overlap between chunks

    Returns:
        Indexing result
    """
    # Ensure persist directory exists
    Path(persist_dir).mkdir(parents=True, exist_ok=True)

    # Load documents
    documents = load_documents(docs_dir)
    if not documents:
        return {
            "success": False,
            "documents_indexed": 0,
            "chunks_created": 0,
            "errors": ["No documents found"],
        }

    # Split into chunks
    chunks = split_documents(documents, chunk_size, chunk_overlap)

    # Create vector store
    create_vectorstore(chunks, persist_dir)

    return {
        "success": True,
        "documents_indexed": len(documents),
        "chunks_created": len(chunks),
        "errors": [],
    }


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Index documents for RAG")
    parser.add_argument("--docs-dir", required=True, help="Documents directory")
    parser.add_argument("--persist-dir", default="data/chroma_db", help="Vector store directory")
    parser.add_argument("--chunk-size", type=int, default=1000, help="Chunk size")
    parser.add_argument("--chunk-overlap", type=int, default=200, help="Chunk overlap")

    args = parser.parse_args()

    result = index_documents(
        docs_dir=args.docs_dir,
        persist_dir=args.persist_dir,
        chunk_size=args.chunk_size,
        chunk_overlap=args.chunk_overlap,
    )

    if result["success"]:
        print(f"Indexed {result['documents_indexed']} documents")
        print(f"Created {result['chunks_created']} chunks")
    else:
        print(f"Indexing failed: {result['errors']}")
        exit(1)


if __name__ == "__main__":
    main()
