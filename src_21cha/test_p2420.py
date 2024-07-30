import pytest
from p2420 import chai


@pytest.mark.parametrize(
    ("a, b, exp"),
    [
        (1, 6, 5),
        (2, 3, 1),
        (5, -2, 7),
    ],
)
def test_add_all(a, b, exp):
    assert chai(a, b) == exp
