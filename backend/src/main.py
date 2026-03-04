import os
from fastapi import FastAPI
from fastapi_docshield import DocShield
from fastapi.middleware.cors import CORSMiddleware
from scalar_fastapi import get_scalar_api_reference

from src.api import register_routes
from src.logs import configure_logging, LogLevels
from src.database.base import Base
from src.database.core import engine

configure_logging(log_level=LogLevels.info)

app = FastAPI(docs_url=None)
register_routes(app=app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(engine)

DOCSHIELD_USERNAME = os.getenv("ADMIN_EMAIL")
DOCSHIELD_PASSWORD = os.getenv("ADMIN_PASSWORD")
DocShield(app=app, credentials={DOCSHIELD_USERNAME: DOCSHIELD_PASSWORD})  # type: ignore


@app.get("/")
def home():
    return {
        "message": "Hello World! This is the home page of the API. Please visit /docs to see the API documentation."
    }


@app.get("/docs", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        # Your OpenAPI document
        openapi_url=app.openapi_url,
        # Avoid CORS issues (optional)
        scalar_proxy_url="https://proxy.scalar.com",
    )
