from fastapi import FastAPI
import uvicorn
from .database import engine
from . import models
from .routers import elements
import logging

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Configure logging
logging.basicConfig(
    filename='api.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Medical Image Processing API")

# Add routers
app.include_router(elements.router, prefix="/api", tags=["elements"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)