"""Backtesting utilities."""
from __future__ import annotations

from pathlib import Path
from typing import Dict

import pandas as pd

from .strategy import scan_value_bets


def run_backtest(path: str | Path) -> Dict[str, float]:
    """Run a naive backtest over snapshot CSV files.

    This function simply loads CSVs, scans for value bets and assumes all bets
    win to provide a best-case PnL. It is intentionally simplistic but provides
    a deterministic function for unit testing.
    """
    path = Path(path)
    pnl = 0.0
    for file in sorted(path.glob("*.csv")):
        df = pd.read_csv(file, parse_dates=["commence_time"])
        signals = scan_value_bets(df)
        pnl += (signals.stake * (signals.odds - 1)).sum()
    return {"pnl": pnl}
