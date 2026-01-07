"""Health check endpoints."""

from fastapi import APIRouter

from src.models import HealthResponse, ReadinessResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Check if the service is healthy.

    Returns:
        Health status
    """
    return HealthResponse(status="healthy")


@router.get("/ready", response_model=ReadinessResponse)
async def readiness_check() -> ReadinessResponse:
    """Check if the service is ready to accept requests.

    This endpoint can include checks for:
    - Database connectivity
    - Model loaded
    - Dependencies available

    Returns:
        Readiness status with individual check results
    """
    checks = {
        "service": True,
        # Add more checks as needed:
        # "database": check_database(),
        # "model": check_model_loaded(),
    }

    all_ready = all(checks.values())

    return ReadinessResponse(
        status="ready" if all_ready else "not_ready",
        checks=checks,
    )
