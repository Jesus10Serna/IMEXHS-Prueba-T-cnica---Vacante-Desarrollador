from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import api_router
from .database import engine
from . import models

# Create tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Medical Image Processing API",
    description="API for managing medical image processing results",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(api_router)