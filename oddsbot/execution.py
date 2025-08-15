"""Execution layer for placing paper bets."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Dict


@dataclass
class PaperBet:
    """Represents a simulated bet."""

    event_id: str
    stake: float
    odds: float
    placed_at: datetime


def place_paper_bet(event_id: str, stake: float, odds: float) -> PaperBet:
    """Create a paper bet ticket."""
    return PaperBet(event_id=event_id, stake=stake, odds=odds, placed_at=datetime.utcnow())
