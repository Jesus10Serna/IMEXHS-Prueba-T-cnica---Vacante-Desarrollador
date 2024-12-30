# Medical Image Processing API

A FastAPI-based REST API for managing medical image processing results.

## Setup

1. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up PostgreSQL and create a .env file with:

```
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_SERVER=localhost
POSTGRES_PORT=5432
POSTGRES_DB=images_db
```

4. Run the application:

```bash
uvicorn app.main:app --reload
```

## API Endpoints

### POST /api/elements/

Create new elements from JSON payload.

### GET /api/elements/

List all elements with optional filters:

- created_after, created_before
- avg_before_min, avg_before_max
- avg_after_min, avg_after_max
- data_size_min, data_size_max

### GET /api/elements/{id}/

Get a specific element by ID.

### PUT /api/elements/{id}/

Update device_name or ID of an existing element.

### DELETE /api/elements/{id}/

Delete an element by ID.

## Features

- Full CRUD operations
- Automatic data normalization
- Comprehensive filtering options
- PostgreSQL database backend
- Request/Response logging
