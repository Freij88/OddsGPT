"""Chart helpers using Plotly."""
from __future__ import annotations

import pandas as pd
import plotly.express as px


def pnl_chart(df: pd.DataFrame):
    """Line chart of PnL over time."""
    if df.empty:
        return px.line()
    return px.line(df, x="time", y="pnl", title="PnL")


def drawdown_chart(df: pd.DataFrame):
    if df.empty:
        return px.line()
    return px.line(df, x="time", y="drawdown", title="Max Drawdown")


def ev_histogram(df: pd.DataFrame):
    if df.empty:
        return px.histogram()
    return px.histogram(df, x="ev", nbins=20, title="EV distribution")


def clv_scatter(df: pd.DataFrame):
    if df.empty:
        return px.scatter()
    return px.scatter(df, x="time", y="clv", title="CLV vs Time")
