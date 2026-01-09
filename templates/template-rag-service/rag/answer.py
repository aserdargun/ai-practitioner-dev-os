"""Answer Generation Module.

Generates answers using retrieved context and LLM.
"""

import argparse
import json
import logging
import os
import sys
from dataclasses import dataclass
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@dataclass
class Answer:
    """Generated answer with metadata."""

    answer: str
    sources: list[str]
    context_used: list[str]
    confidence: float | None = None


class AnswerGenerator:
    """Generates answers using LLM with retrieved context.

    Replace the LLM call with your preferred provider:
    - OpenAI
    - Anthropic
    - Local models (Ollama, vLLM)
    """

    def __init__(
        self,
        model: str = "gpt-3.5-turbo",
        max_context_length: int = 3000,
    ):
        self.model = model
        self.max_context_length = max_context_length

    def build_prompt(
        self,
        query: str,
        context: list[dict],
    ) -> str:
        """Build the prompt with context and query."""
        # Truncate context if needed
        context_text = ""
        for ctx in context:
            chunk = f"\n---\nSource: {ctx.get('source', 'unknown')}\n{ctx['content']}\n"
            if len(context_text) + len(chunk) > self.max_context_length:
                break
            context_text += chunk

        prompt = f"""Answer the following question based on the provided context.
If the context doesn't contain enough information, say so.

Context:
{context_text}

Question: {query}

Answer:"""

        return prompt

    def generate(
        self,
        query: str,
        context: list[dict],
    ) -> Answer:
        """Generate an answer using context.

        Replace this with actual LLM API call.
        """
        logger.info(f"Generating answer for: {query[:50]}...")

        prompt = self.build_prompt(query, context)

        # Placeholder: Replace with actual LLM call
        # Example with OpenAI:
        #   from openai import OpenAI
        #   client = OpenAI()
        #   response = client.chat.completions.create(
        #       model=self.model,
        #       messages=[{"role": "user", "content": prompt}]
        #   )
        #   answer_text = response.choices[0].message.content

        # Demo: Simple extractive answer
        if context:
            # Use first context chunk as demo answer
            answer_text = (
                f"Based on the provided context about '{query}': "
                f"{context[0]['content'][:200]}..."
            )
        else:
            answer_text = (
                "I don't have enough context to answer this question. "
                "Please provide relevant documents or rephrase your query."
            )

        sources = [ctx.get("source", "unknown") for ctx in context]
        context_used = [ctx["content"][:100] + "..." for ctx in context]

        return Answer(
            answer=answer_text,
            sources=sources,
            context_used=context_used,
            confidence=0.8 if context else 0.2,
        )


def generate_answer(
    query: str,
    store_path: str = "vectorstore",
    top_k: int = 5,
    model: str = "gpt-3.5-turbo",
) -> dict:
    """Generate an answer for a query.

    This is the main entry point that combines retrieval and generation.

    Args:
        query: The user's question
        store_path: Path to vector store
        top_k: Number of context chunks to retrieve
        model: LLM model to use

    Returns:
        Answer dictionary with response and metadata
    """
    # Import here to avoid circular imports
    from retrieve import retrieve_context

    # Retrieve relevant context
    context = retrieve_context(
        query=query,
        store_path=store_path,
        top_k=top_k,
    )

    # Generate answer
    generator = AnswerGenerator(model=model)
    answer = generator.generate(query, context)

    return {
        "query": query,
        "answer": answer.answer,
        "sources": answer.sources,
        "confidence": answer.confidence,
        "context_chunks": len(context),
    }


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Generate RAG answer")
    parser.add_argument(
        "--query",
        type=str,
        required=True,
        help="Question to answer",
    )
    parser.add_argument(
        "--store",
        type=str,
        default="vectorstore",
        help="Vector store path",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=5,
        help="Number of context chunks to retrieve",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=os.getenv("COMPLETION_MODEL", "gpt-3.5-turbo"),
        help="LLM model to use",
    )
    args = parser.parse_args()

    result = generate_answer(
        query=args.query,
        store_path=args.store,
        top_k=args.top_k,
        model=args.model,
    )

    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
