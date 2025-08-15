"""Form components for configuration and filters."""
from __future__ import annotations

import streamlit as st

from oddsbot.config import settings


def settings_form() -> None:
    """Display and edit basic settings."""
    st.subheader("Settings")
    with st.form("settings_form"):
        min_ev = st.number_input("Min EV", value=settings.min_ev)
        kelly = st.number_input("Kelly factor", value=settings.kelly_factor)
        submitted = st.form_submit_button("Save")
    if submitted:
        settings.min_ev = float(min_ev)
        settings.kelly_factor = float(kelly)
        st.success("Settings updated (not persisted)")
