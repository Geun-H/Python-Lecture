import pytest
from p11382 import add_all


@pytest.mark.parametrize(
    ("a, b, c, exp"),
    [
        (1, 2, 3, 6),
        (2, 2, 2, 6),
        (5, 5, 5, 15),
    ],
)
def test_add_all(a, b, c, exp):
    assert add_all(a, b, c) == exp
