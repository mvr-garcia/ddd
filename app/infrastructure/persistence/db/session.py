
from typing import Optional

import orjson

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.settings import Settings

_engine: Optional[AsyncEngine] = None
_maker: Optional[sessionmaker] = None

async def get_engine(*, settings: Settings) -> AsyncEngine:
    global _engine
    
    if _engine is None:
        
        def json_dumps(obj):
            return orjson.dumps(obj).decode()
        
        engine_options = {
            "echo": settings.DATABASE_ECHO_SQL,
            "json_serializer": json_dumps,
            "json_deserializer": orjson.loads,
            "isolation_level": settings.DATABASE_ISOLATION_LEVEL,
            "max_overflow": settings.DATABASE_MAX_OVERFLOW,
            "pool_size": settings.DATABASE_POOL_SIZE,
            "pool_recycle": settings.DATABASE_POOL_RECYCLE_SECONDS,
            "pool_pre_ping": settings.DATABASE_POOL_PRE_PING,
        }

        _engine = create_async_engine(url=settings.DATABASE_URL, **engine_options)

    return _engine


async def get_session_maker(*, engine: AsyncEngine) -> sessionmaker:
    global _maker
    
    if _maker is None:
        _maker = sessionmaker(
            bind=engine,
            class_=AsyncSession,
            autoflush=False,
            autocommit=False,
            expire_on_commit=True,
        )

    return _maker


async def dispose_engine() -> None:
    global _engine, _maker

    if _engine:
        await _engine.dispose()
        _engine = None
        _maker = None
