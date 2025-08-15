"""Database persistence helpers."""
from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path

from sqlmodel import Session, SQLModel, create_engine

DATABASE_URL = "sqlite:///data/oddsbot.db"
DB_PATH = Path("data")
DB_PATH.mkdir(exist_ok=True)

engine = create_engine(DATABASE_URL, echo=False)


def init_db() -> None:
    """Create database tables."""
    SQLModel.metadata.create_all(engine)


@contextmanager
def get_session() -> Session:
    """Provide a transactional scope around a series of operations."""
    with Session(engine) as session:
        yield session
