"""KPI card components."""
from __future__ import annotations

import streamlit as st


def show_kpis(bankroll: float, pnl_day: float, pnl_total: float, exposure: float, bets: int) -> None:
    """Display KPI cards in a five-column layout."""
    cols = st.columns(5)
    data = [
        ("Bankroll", bankroll),
        ("PnL Today", pnl_day),
        ("PnL Total", pnl_total),
        ("Exposure", exposure),
        ("Bets", bets),
    ]
    for col, (label, value) in zip(cols, data):
        col.metric(label, f"{value:.2f}" if isinstance(value, (int, float)) else value)
