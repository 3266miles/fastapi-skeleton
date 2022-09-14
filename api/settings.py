import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    version: str = "0.1.0"
    log_level: str = os.environ.get("LOG_LEVEL", "INFO")


settings = Settings()
