"""
Application settings.
"""

import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # Environment
    ENVIRONMENT_NAME: str = "development"

    # Database configuration
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/app_db"
    DATABASE_ECHO_SQL: bool = False
    DATABASE_ISOLATION_LEVEL: str = "READ COMMITTED"
    DATABASE_POOL_SIZE: int = 5
    DATABASE_MAX_OVERFLOW: int = 10
    DATABASE_POOL_RECYCLE_SECONDS: int = 1800
    DATABASE_POOL_PRE_PING: bool = True
