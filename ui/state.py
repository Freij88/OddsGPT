"""Session state helpers for Streamlit UI."""
from __future__ import annotations

import streamlit as st


def init_state() -> None:
    """Initialise default session state values."""
    defaults = {
        "is_running": False,
        "signals": None,
        "bets": None,
    }
    for key, value in defaults.items():
        st.session_state.setdefault(key, value)
