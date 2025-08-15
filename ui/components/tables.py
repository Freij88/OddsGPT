"""Table rendering helpers."""
from __future__ import annotations

import pandas as pd
import streamlit as st


def build_signals_table(df: pd.DataFrame) -> None:
    """Render signals DataFrame with basic formatting."""
    if df.empty:
        st.info("Inga signaler ännu")
        return
    st.dataframe(df)
