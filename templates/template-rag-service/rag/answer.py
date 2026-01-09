"""
Answer Generation Module

Generates answers based on retrieved context.
"""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AnswerGenerator:
    """Generate answers using retrieved context."""

    def __init__(self, model: str = None):
        """
        Initialize answer generator.

        Args:
            model: LLM model to use (placeholder for future use)
        """
        self.model = model or "template"

    def generate(
        self,
        query: str,
        context: list[dict],
        max_context_length: int = 2000,
    ) -> dict:
        """
        Generate an answer based on query and context.

        This is a template implementation. Replace with actual LLM call
        in production (OpenAI, Anthropic, local model, etc.).

        Args:
            query: User query
            context: List of retrieved documents
            max_context_length: Maximum context length

        Returns:
            Answer dict with text and sources
        """
        if not context:
            return {
                "answer": "I couldn't find relevant information to answer your question.",
                "sources": [],
                "confidence": 0.0,
            }

        # Combine context
        context_texts = []
        total_length = 0

        for doc in context:
            text = doc.get("text", "")
            if total_length + len(text) <= max_context_length:
                context_texts.append(text)
                total_length += len(text)

        combined_context = "\n\n".join(context_texts)

        # Template: Return context summary
        # In production, replace with actual LLM call:
        #
        # response = openai.chat.completions.create(
        #     model="gpt-4",
        #     messages=[
        #         {"role": "system", "content": "Answer based on context."},
        #         {"role": "user", "content": f"Context:\n{combined_context}\n\nQuestion: {query}"}
        #     ]
        # )
        # answer_text = response.choices[0].message.content

        # Placeholder answer
        answer_text = self._template_answer(query, combined_context, context)

        # Extract sources
        sources = [
            {
                "source": doc["metadata"]["source"],
                "score": doc.get("score", 0.0),
            }
            for doc in context
            if "metadata" in doc
        ]

        # Calculate confidence (placeholder)
        avg_score = sum(doc.get("score", 0) for doc in context) / len(context)

        return {
            "answer": answer_text,
            "sources": sources,
            "confidence": avg_score,
        }

    def _template_answer(
        self,
        query: str,
        context: str,
        docs: list[dict],
    ) -> str:
        """
        Generate a template answer (placeholder).

        Replace this with actual LLM integration.

        Args:
            query: User query
            context: Combined context text
            docs: Retrieved documents

        Returns:
            Answer text
        """
        # Simple extractive answer based on context
        # This is just a placeholder - use an LLM in production

        sentences = context.replace("\n", " ").split(".")
        relevant_sentences = []

        query_words = set(query.lower().split())

        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue

            sentence_words = set(sentence.lower().split())
            overlap = len(query_words & sentence_words)

            if overlap >= 2:
                relevant_sentences.append(sentence)

        if relevant_sentences:
            answer = ". ".join(relevant_sentences[:3]) + "."
        else:
            answer = f"Based on the documents, I found relevant information about: {query}"

        return answer


def generate_answer(query: str, context: list[dict]) -> dict:
    """
    Convenience function for generating answers.

    Args:
        query: User query
        context: Retrieved documents

    Returns:
        Answer dict
    """
    generator = AnswerGenerator()
    return generator.generate(query, context)


def rag_query(query: str, top_k: int = 5) -> dict:
    """
    End-to-end RAG query.

    Args:
        query: User query
        top_k: Number of documents to retrieve

    Returns:
        Answer dict with sources
    """
    from rag.retrieve import Retriever

    # Retrieve
    retriever = Retriever()
    docs = retriever.search(query, top_k=top_k)

    # Generate
    generator = AnswerGenerator()
    result = generator.generate(query, docs)

    return result


if __name__ == "__main__":
    # Simple CLI for testing
    import sys

    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        result = rag_query(query)

        print(f"\nQuery: {query}")
        print(f"\nAnswer: {result['answer']}")
        print(f"\nConfidence: {result['confidence']:.2f}")
        print(f"\nSources:")
        for source in result["sources"]:
            print(f"  - {source['source']} (score: {source['score']:.3f})")
    else:
        print("Usage: python -m rag.answer <query>")
