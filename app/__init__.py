from fastapi import FastAPI

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

from app.api import *
from app.schema import generate_schema
openapi_schema = generate_schema(app)

from . import agent


@app.get("/openapi.json", tags=["documentation"], include_in_schema=False)
async def openapi():
    return openapi_schema


