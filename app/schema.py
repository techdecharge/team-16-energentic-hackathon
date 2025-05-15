from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI
from app.config import APPLICATION_HOST, APPLICATION_PORT


def generate_schema(app: FastAPI):
    return get_openapi(
        title="My API",
        version="1.0",
        description="Auto-generated spec",
        routes=app.routes,
        servers=[{"url": f"http://{APPLICATION_HOST}:{APPLICATION_PORT}", "description": "Local development server"}]
    )

