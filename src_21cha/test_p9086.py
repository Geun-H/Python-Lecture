import pytest
from p9086 import pick_fl


@pytest.mark.parametrize(
    ("word, exp"),
    [
        ("AAOE", "AE"),
        ("AEO", "AO"),
        ("O", "OO"),
    ],
)
def test_pick(word, exp):
    assert pick_fl(word) == exp
