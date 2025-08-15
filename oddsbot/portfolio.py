"""Portfolio management helpers."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Portfolio:
    """Simple bankroll tracker."""

    bankroll: float = 1000.0

    def apply_result(self, result: float) -> None:
        """Update bankroll with profit/loss."""
        self.bankroll += result

    def exposure(self) -> float:
        """Current exposure is 0 for paper trading."""
        return 0.0
