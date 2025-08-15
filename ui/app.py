"""Streamlit dashboard for OddsBot."""
from __future__ import annotations

import asyncio
from datetime import datetime

import pandas as pd
import streamlit as st

from oddsbot.strategy import scan_value_bets
from .state import init_state
from .components.kpi_cards import show_kpis
from .components.tables import build_signals_table
from .components.forms import settings_form
from .components.charts import pnl_chart, drawdown_chart, ev_histogram, clv_scatter
from .components.log_viewer import show_logs

st.set_page_config(page_title="OddsBot", layout="wide")
init_state()


def dashboard_page():
    st.title("Dashboard")
    show_kpis(1000, 0, 0, 0, 0)
    st.plotly_chart(pnl_chart(pd.DataFrame()), use_container_width=True)
    st.plotly_chart(drawdown_chart(pd.DataFrame()), use_container_width=True)
    st.plotly_chart(ev_histogram(pd.DataFrame()), use_container_width=True)
    st.plotly_chart(clv_scatter(pd.DataFrame()), use_container_width=True)


def live_page():
    st.title("Live Scanner")
    if st.button("Start"):
        st.session_state.is_running = True
    if st.button("Stop"):
        st.session_state.is_running = False
    if st.session_state.is_running:
        st.info("Live scanning not implemented in demo")
    build_signals_table(pd.DataFrame())
    show_logs()


def signals_page():
    st.title("Signals & Bets")
    build_signals_table(pd.DataFrame())


def portfolio_page():
    st.title("Portfolio & Risk")
    st.write("Bankroll: 1000")


def backtest_page():
    st.title("Backtest")
    st.info("Upload snapshot CSVs to run backtest (not implemented)")


def settings_page():
    st.title("Settings")
    settings_form()


PAGES = {
    "Dashboard": dashboard_page,
    "Live": live_page,
    "Signals": signals_page,
    "Portfolio": portfolio_page,
    "Backtest": backtest_page,
    "Settings": settings_page,
}


def main() -> None:
    page = st.sidebar.selectbox("Navigate", list(PAGES))
    PAGES[page]()


if __name__ == "__main__":
    main()
