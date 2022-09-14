import logging
import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import all_routers
from .settings import settings

logging.basicConfig(stream=sys.stdout, level=settings.log_level)
log = logging.getLogger(__name__)

app = FastAPI(
    title="REST API Skeleton",
    description="A FastAPI REST API skeleton with HTTP2 support",
    version=settings.version,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

origins = [
    "http://localhost:8080",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)


@app.on_event("startup")
def on_startup():
    log.info(f"Starting Slide App API service - version: {settings.version}")
    log.info(settings)


for router in all_routers:
    app.include_router(router)


@app.get("/", name="Base", include_in_schema=False)
async def root():
    return {"message": "Hell World!"}


@app.get("/healthz", include_in_schema=False)
async def healthcheck():
    return {"msg": "ok"}
