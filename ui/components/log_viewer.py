"""Simple log viewer component."""
from __future__ import annotations

from pathlib import Path

import streamlit as st

LOG_PATH = Path("logs/app.log")


def show_logs(lines: int = 20) -> None:
    """Display last N lines from log file."""
    if LOG_PATH.exists():
        content = LOG_PATH.read_text().splitlines()[-lines:]
        st.text("\n".join(content))
    else:
        st.info("No logs yet")
