from oddsbot.vig import remove_vig


def test_remove_vig_sums_to_one():
    probs = remove_vig([1.91, 1.91])
    assert abs(sum(probs) - 1) < 1e-9
