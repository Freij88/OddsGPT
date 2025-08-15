"""Bet selection logic."""
from __future__ import annotations

from datetime import datetime, timedelta
from typing import Iterable

import pandas as pd

from .config import settings
from .pricing import expected_value, kelly_stake


def scan_value_bets(df: pd.DataFrame, now: datetime | None = None) -> pd.DataFrame:
    """Return DataFrame of value bets based on settings.

    Parameters
    ----------
    df: DataFrame
        Must contain columns: odds, fair_prob, commence_time.
    now: datetime
        Reference time, default UTC now.
    """
    if df.empty:
        return df
    now = now or datetime.utcnow()
    df = df.copy()
    df["ev"] = df.apply(lambda r: expected_value(r.odds, r.fair_prob), axis=1)
    df["stake"] = df.apply(
        lambda r: kelly_stake(
            bankroll=1000.0,  # placeholder bankroll for scanning
            odds=r.odds,
            fair_prob=r.fair_prob,
            kelly_factor=settings.kelly_factor,
            max_pct=settings.max_bet_pct,
        ),
        axis=1,
    )
    df = df[df.ev > settings.min_ev]
    df = df[(df.odds >= settings.min_odds) & (df.odds <= settings.max_odds)]
    df = df[df.commence_time - now >= timedelta(minutes=settings.min_time_to_start)]
    return df


def filter_by_sport(df: pd.DataFrame, sports: Iterable[str]) -> pd.DataFrame:
    """Return dataframe filtered by sport list."""
    if not sports:
        return df
    return df[df.sport.isin(sports)]
