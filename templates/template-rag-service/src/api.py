"""FastAPI application for RAG service."""

from fastapi import FastAPI, HTTPException

from src.models import QueryRequest, QueryResponse
from src.rag import get_rag_chain

app = FastAPI(
    title="RAG Service",
    description="Retrieval-Augmented Generation service for document Q&A",
    version="0.1.0",
)


@app.get("/")
async def root() -> dict:
    """Root endpoint."""
    return {"message": "RAG Service", "version": "0.1.0"}


@app.get("/health")
async def health() -> dict:
    """Health check endpoint."""
    return {"status": "healthy"}


@app.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest) -> QueryResponse:
    """Query the RAG system.

    Args:
        request: Query request with question

    Returns:
        Generated answer with sources
    """
    try:
        rag = get_rag_chain()
        result = rag.query(request.question, top_k=request.top_k)

        return QueryResponse(
            answer=result["answer"],
            sources=result["sources"],
            confidence=result["confidence"],
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/stats")
async def stats() -> dict:
    """Get vector store statistics."""
    try:
        rag = get_rag_chain()
        if rag.vectorstore:
            collection = rag.vectorstore._collection
            return {
                "documents_count": collection.count(),
                "persist_dir": rag.persist_dir,
            }
        return {"documents_count": 0, "persist_dir": None}
    except Exception as e:
        return {"error": str(e)}
