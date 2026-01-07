"""Response generation for RAG.

This module provides a placeholder for LLM integration.
Replace the implementation with your preferred LLM provider.
"""


def generate_response(context: str, question: str) -> str:
    """Generate a response using the context and question.

    This is a placeholder implementation. Replace with your LLM of choice:
    - OpenAI API
    - Anthropic API
    - Local models (Ollama, vLLM, etc.)
    - HuggingFace models

    Args:
        context: Retrieved context from vector search.
        question: User's question.

    Returns:
        Generated response string.

    Example implementation with OpenAI:
        ```python
        import openai

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"Answer based on this context:\\n\\n{context}"
                },
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content
        ```
    """
    # Placeholder: return context summary
    # Replace this with actual LLM call
    context_preview = context[:500] + "..." if len(context) > 500 else context

    return (
        f"[LLM Integration Required]\n\n"
        f"Question: {question}\n\n"
        f"Retrieved Context:\n{context_preview}\n\n"
        f"To enable AI-generated responses, implement an LLM provider in "
        f"rag/generator.py"
    )


def generate_with_sources(
    context: str, question: str, source_refs: list[str]
) -> tuple[str, list[str]]:
    """Generate response with source citations.

    Args:
        context: Retrieved context.
        question: User's question.
        source_refs: List of source references.

    Returns:
        Tuple of (response, cited_sources).
    """
    response = generate_response(context, question)
    return response, source_refs
