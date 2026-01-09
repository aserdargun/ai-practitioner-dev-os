"""Answer generation for RAG."""

import json
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

from rag.retrieve import Retriever, RetrievalResult

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class Source:
    """Source citation for an answer."""

    chunk_id: str
    content: str
    relevance_score: float


@dataclass
class RAGResponse:
    """Response from RAG system."""

    query: str
    answer: str
    sources: List[Source]
    confidence: float


class MockLLM:
    """Mock LLM for demonstration.

    Replace with actual LLM (OpenAI, Anthropic, local model, etc.)
    """

    def generate(self, prompt: str, max_tokens: int = 500) -> str:
        """Generate response from prompt.

        This is a mock implementation that creates a simple response
        based on the context provided. Replace with actual LLM in production.
        """
        # Extract context from prompt
        if "Context:" in prompt and "Question:" in prompt:
            context_start = prompt.find("Context:") + len("Context:")
            context_end = prompt.find("Question:")
            context = prompt[context_start:context_end].strip()

            question_start = prompt.find("Question:") + len("Question:")
            question = prompt[question_start:].strip()

            # Generate mock response based on context
            if context:
                # Take first few sentences of context as mock answer
                sentences = context.split(".")[:2]
                answer = ". ".join(sentences).strip()
                if answer and not answer.endswith("."):
                    answer += "."
                return f"Based on the provided context: {answer}"

        return "I don't have enough context to answer this question accurately."


class RAGAnswerer:
    """Generates answers using retrieval-augmented generation."""

    def __init__(
        self,
        retriever: Retriever,
        llm: Optional[MockLLM] = None,
        top_k: int = 5,
    ):
        """Initialize the RAG answerer.

        Args:
            retriever: Retriever instance for finding relevant chunks
            llm: Language model for generation (defaults to MockLLM)
            top_k: Number of chunks to retrieve
        """
        self.retriever = retriever
        self.llm = llm or MockLLM()
        self.top_k = top_k

    def answer(
        self,
        query: str,
        min_score: float = 0.0,
    ) -> RAGResponse:
        """Generate an answer for a query.

        Args:
            query: User's question
            min_score: Minimum relevance score for sources

        Returns:
            RAGResponse with answer and sources
        """
        logger.info(f"Processing query: {query}")

        # Retrieve relevant chunks
        results = self.retriever.search(
            query=query,
            top_k=self.top_k,
            min_score=min_score,
        )

        if not results:
            return RAGResponse(
                query=query,
                answer="I couldn't find relevant information to answer this question.",
                sources=[],
                confidence=0.0,
            )

        # Build context from retrieved chunks
        context = self._build_context(results)

        # Generate answer
        prompt = self._build_prompt(query, context)
        raw_answer = self.llm.generate(prompt)

        # Build response
        sources = [
            Source(
                chunk_id=r.chunk_id,
                content=r.content[:200] + "..." if len(r.content) > 200 else r.content,
                relevance_score=r.score,
            )
            for r in results
        ]

        # Confidence based on top retrieval score
        confidence = results[0].score if results else 0.0

        return RAGResponse(
            query=query,
            answer=raw_answer,
            sources=sources,
            confidence=confidence,
        )

    def _build_context(self, results: List[RetrievalResult]) -> str:
        """Build context string from retrieval results."""
        context_parts = []
        for i, result in enumerate(results, 1):
            context_parts.append(f"[{i}] {result.content}")
        return "\n\n".join(context_parts)

    def _build_prompt(self, query: str, context: str) -> str:
        """Build prompt for LLM."""
        return f"""Answer the question based on the provided context. If the context doesn't contain relevant information, say so.

Context:
{context}

Question: {query}

Answer:"""


def evaluate_golden_set(
    answerer: RAGAnswerer,
    golden_path: str,
) -> dict:
    """Evaluate RAG system against golden set.

    Args:
        answerer: RAGAnswerer instance
        golden_path: Path to golden set JSONL file

    Returns:
        Evaluation metrics
    """
    path = Path(golden_path)
    if not path.exists():
        raise FileNotFoundError(f"Golden set not found: {golden_path}")

    results = []
    with open(path, "r") as f:
        for line in f:
            test_case = json.loads(line)
            query = test_case["query"]

            response = answerer.answer(query)

            result = {
                "query": query,
                "expected": test_case.get("expected_answer", ""),
                "actual": response.answer,
                "confidence": response.confidence,
                "num_sources": len(response.sources),
            }
            results.append(result)

    # Compute metrics
    total = len(results)
    avg_confidence = sum(r["confidence"] for r in results) / total if total > 0 else 0
    avg_sources = sum(r["num_sources"] for r in results) / total if total > 0 else 0

    return {
        "total_queries": total,
        "average_confidence": round(avg_confidence, 3),
        "average_sources": round(avg_sources, 1),
        "results": results,
    }


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="RAG Answer Generation")
    parser.add_argument("--query", "-q", help="Query to answer")
    parser.add_argument("--index", "-i", default="index/", help="Index directory")
    parser.add_argument("--eval", "-e", help="Golden set path for evaluation")
    parser.add_argument("--top-k", type=int, default=5, help="Number of chunks")

    args = parser.parse_args()

    retriever = Retriever(index_path=args.index)
    answerer = RAGAnswerer(retriever, top_k=args.top_k)

    if args.eval:
        # Run evaluation
        metrics = evaluate_golden_set(answerer, args.eval)
        print(json.dumps(metrics, indent=2))
    elif args.query:
        # Answer single query
        response = answerer.answer(args.query)
        print(f"Query: {response.query}")
        print(f"Answer: {response.answer}")
        print(f"Confidence: {response.confidence:.2f}")
        print(f"Sources: {len(response.sources)}")
        for i, source in enumerate(response.sources, 1):
            print(f"  [{i}] Score: {source.relevance_score:.2f}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
