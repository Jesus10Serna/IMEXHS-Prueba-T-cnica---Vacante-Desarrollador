from fastapi import APIRouter
from .elements import router as elements_router

# Create main router
api_router = APIRouter()

# Include routes
api_router.include_router(elements_router, prefix="/api/elements", tags=["elements"])