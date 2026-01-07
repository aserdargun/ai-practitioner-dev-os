"""Pydantic models for RAG service."""

from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    """Request model for RAG queries."""

    question: str = Field(..., min_length=1, description="Question to answer")
    top_k: int = Field(default=4, ge=1, le=10, description="Number of documents to retrieve")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"question": "What is the main topic of the documents?", "top_k": 4}
            ]
        }
    }


class QueryResponse(BaseModel):
    """Response model for RAG queries."""

    answer: str = Field(..., description="Generated answer")
    sources: list[str] = Field(default_factory=list, description="Source documents used")
    confidence: float = Field(default=0.0, description="Confidence score")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "answer": "The main topic is machine learning.",
                    "sources": ["doc1.txt", "doc2.txt"],
                    "confidence": 0.85,
                }
            ]
        }
    }


class IndexRequest(BaseModel):
    """Request model for document indexing."""

    docs_dir: str = Field(..., description="Directory containing documents")
    chunk_size: int = Field(default=1000, ge=100, description="Chunk size for splitting")
    chunk_overlap: int = Field(default=200, ge=0, description="Overlap between chunks")


class IndexResponse(BaseModel):
    """Response model for indexing."""

    success: bool = Field(..., description="Whether indexing succeeded")
    documents_indexed: int = Field(default=0, description="Number of documents indexed")
    chunks_created: int = Field(default=0, description="Number of chunks created")
    errors: list[str] = Field(default_factory=list, description="Errors encountered")


class EvaluationResult(BaseModel):
    """Result of RAG evaluation."""

    faithfulness: float = Field(..., description="Faithfulness score")
    answer_relevancy: float = Field(..., description="Answer relevancy score")
    context_precision: float = Field(..., description="Context precision score")
    context_recall: float = Field(..., description="Context recall score")
    overall: float = Field(..., description="Overall score")
