"""Database models using SQLModel."""
from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Snapshot(SQLModel, table=True):
    """Snapshot of odds fetched from API."""

    id: Optional[int] = Field(default=None, primary_key=True)
    fetched_at: datetime = Field(default_factory=datetime.utcnow)
    data: str  # JSON blob of odds


class Signal(SQLModel, table=True):
    """Betting signal identified by strategy."""

    id: Optional[int] = Field(default=None, primary_key=True)
    event_id: str
    sport: str
    market: str
    bookmaker: str
    odds: float
    fair_prob: float
    ev: float
    created_at: datetime = Field(default_factory=datetime.utcnow)
    expires_at: datetime


class Ticket(SQLModel, table=True):
    """Paper bet ticket."""

    id: Optional[int] = Field(default=None, primary_key=True)
    signal_id: int
    stake: float
    odds: float
    placed_at: datetime = Field(default_factory=datetime.utcnow)
    settled: bool = False
    result: Optional[float] = None  # profit/loss


class Portfolio(SQLModel, table=True):
    """Portfolio metrics."""

    id: Optional[int] = Field(default=None, primary_key=True)
    bankroll: float = 0.0
    updated_at: datetime = Field(default_factory=datetime.utcnow)
