from oddsbot.pricing import expected_value, kelly_stake


def test_ev_and_kelly():
    odds = 2.0
    fair_prob = 0.55
    ev = expected_value(odds, fair_prob)
    assert ev == odds * fair_prob - 1
    stake = kelly_stake(1000, odds, fair_prob, kelly_factor=0.25, max_pct=0.05)
    assert 0 < stake <= 50
