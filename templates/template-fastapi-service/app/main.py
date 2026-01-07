"""FastAPI application entry point."""

from fastapi import FastAPI

from app.routes import router

app = FastAPI(
    title="ML Service",
    description="Machine Learning Model API",
    version="0.1.0",
)

app.include_router(router)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
