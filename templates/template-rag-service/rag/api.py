"""FastAPI endpoints for RAG service."""

import os
from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from rag.chunker import chunk_text
from rag.embedder import Embedder
from rag.generator import generate_response
from rag.retriever import Retriever

app = FastAPI(
    title="RAG Service",
    description="Retrieval-Augmented Generation API",
    version="0.1.0",
)

# Initialize components
embedder = Embedder()
retriever = Retriever(embedder)


class IngestRequest(BaseModel):
    """Document ingestion request."""

    text: str = Field(..., description="Document text to ingest")
    metadata: dict[str, Any] = Field(
        default_factory=dict, description="Document metadata"
    )


class SearchRequest(BaseModel):
    """Search request."""

    query: str = Field(..., description="Search query")
    top_k: int = Field(default=5, ge=1, le=100, description="Number of results")


class SearchResult(BaseModel):
    """Single search result."""

    text: str
    score: float
    metadata: dict[str, Any]


class SearchResponse(BaseModel):
    """Search response."""

    results: list[SearchResult]


class QueryRequest(BaseModel):
    """RAG query request."""

    question: str = Field(..., description="Question to answer")
    top_k: int = Field(default=5, ge=1, le=20, description="Context chunks to use")


class QueryResponse(BaseModel):
    """RAG query response."""

    answer: str
    sources: list[SearchResult]


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "documents": retriever.document_count}


@app.post("/ingest")
async def ingest_document(request: IngestRequest):
    """Ingest a document into the vector store."""
    try:
        chunks = chunk_text(request.text)
        for i, chunk in enumerate(chunks):
            chunk_metadata = {
                **request.metadata,
                "chunk_index": i,
                "total_chunks": len(chunks),
            }
            retriever.add_document(chunk, chunk_metadata)

        return {
            "status": "success",
            "chunks_created": len(chunks),
            "total_documents": retriever.document_count,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/search", response_model=SearchResponse)
async def search(request: SearchRequest):
    """Perform semantic search."""
    try:
        results = retriever.search(request.query, top_k=request.top_k)
        return SearchResponse(
            results=[
                SearchResult(text=r["text"], score=r["score"], metadata=r["metadata"])
                for r in results
            ]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    """Perform RAG query (search + generate)."""
    try:
        # Retrieve relevant context
        results = retriever.search(request.question, top_k=request.top_k)

        if not results:
            return QueryResponse(
                answer="I couldn't find relevant information to answer your question.",
                sources=[],
            )

        # Build context from results
        context = "\n\n".join([r["text"] for r in results])

        # Generate response
        answer = generate_response(context, request.question)

        return QueryResponse(
            answer=answer,
            sources=[
                SearchResult(text=r["text"], score=r["score"], metadata=r["metadata"])
                for r in results
            ],
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/documents")
async def list_documents():
    """List indexed documents."""
    return {
        "count": retriever.document_count,
        "documents": retriever.get_all_metadata(),
    }
