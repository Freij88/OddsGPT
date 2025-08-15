"""Utilities for removing the bookmaker's vig."""
from __future__ import annotations

from typing import Iterable, List

import numpy as np


def remove_vig(odds: Iterable[float]) -> List[float]:
    """Convert offered odds to fair probabilities without vig.

    Parameters
    ----------
    odds:
        Iterable of decimal odds.

    Returns
    -------
    list of float
        Normalised probabilities that sum to 1.
    """
    odds_arr = np.asarray(list(odds), dtype=float)
    if np.any(odds_arr <= 1):
        raise ValueError("Odds must be greater than 1")
    implied = 1 / odds_arr
    total = implied.sum()
    return list(implied / total)


def fair_odds(odds: Iterable[float]) -> List[float]:
    """Return vig-free odds corresponding to input odds."""
    probs = remove_vig(odds)
    return [1 / p for p in probs]
