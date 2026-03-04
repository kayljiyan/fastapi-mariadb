from os import getenv
from functools import lru_cache

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

if getenv("ENVIRONMENT") != "production":
    load_dotenv()

DATABASE_URL = getenv("MARIADB_CONNECTION_STRING")


@lru_cache(maxsize=1)
def get_engine():
    try:
        engine = create_engine(
            DATABASE_URL,
            pool_size=10,
            max_overflow=20,
            pool_pre_ping=True,  # Prevents stale connections
            pool_recycle=3600,
        )
        return engine

    except OperationalError as e:
        raise e


# Create session factory
engine = get_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
