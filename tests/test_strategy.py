from datetime import datetime, timedelta

import pandas as pd

from oddsbot.strategy import scan_value_bets
from oddsbot.config import settings


def test_scan_filters_ev_and_odds():
    now = datetime.utcnow()
    df = pd.DataFrame(
        {
            "odds": [2.0, 1.5],
            "fair_prob": [0.6, 0.7],
            "commence_time": [now + timedelta(hours=1), now + timedelta(hours=1)],
            "sport": ["soccer", "soccer"],
        }
    )
    original_min_ev = settings.min_ev
    try:
        settings.min_ev = 0.02
        result = scan_value_bets(df, now)
    finally:
        settings.min_ev = original_min_ev
    assert len(result) == 1
