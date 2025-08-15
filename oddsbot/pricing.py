"""Pricing helpers for betting calculations."""
from __future__ import annotations

from typing import Iterable

import numpy as np

from .vig import remove_vig


def implied_prob(odds: float) -> float:
    """Return implied probability from decimal odds."""
    if odds <= 1:
        raise ValueError("Odds must be greater than 1")
    return 1 / odds


def fair_probabilities(odds: Iterable[float]) -> np.ndarray:
    """Return vig-free probabilities for iterable of odds."""
    return np.array(remove_vig(odds))


def expected_value(odds: float, fair_prob: float) -> float:
    """Compute expected value of a bet."""
    return odds * fair_prob - 1


def kelly_fraction(odds: float, fair_prob: float) -> float:
    """Full Kelly fraction for given odds and probability."""
    b = odds - 1
    return (odds * fair_prob - (1 - fair_prob)) / b


def kelly_stake(
    bankroll: float,
    odds: float,
    fair_prob: float,
    kelly_factor: float = 0.25,
    max_pct: float = 0.05,
) -> float:
    """Return stake size based on fractional Kelly with caps."""
    f = kelly_fraction(odds, fair_prob) * kelly_factor
    f = max(0.0, min(f, max_pct))
    return bankroll * f
