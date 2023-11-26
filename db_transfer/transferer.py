import os
import sys

from sqlalchemy import create_engine, schema, Column, Integer, String, DateTime, Boolean
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, BOOLEAN
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base

from .constants import POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT

DATABASE_NAME = 'postgres'

Base = declarative_base()


def initialize_bd(bd_path: str) -> None:

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{bd_path}"

    engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.create_all(engine)


def get_sqlite_engine(bd_path: str) -> AsyncEngine:

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{bd_path}"

    engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)

    return engine


def get_postgres_engine() -> AsyncEngine:
    url = f'postgresql://postgres:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{DATABASE_NAME}'
    print(f"{url=}")
    postgres_engine = create_engine(url)
    return postgres_engine


async def create_tables(engine):

    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    except Exception:
        pass
    finally:
        return

def get_session(engine: AsyncEngine):
    sessionmaker = async_sessionmaker(engine)
    return sessionmaker


