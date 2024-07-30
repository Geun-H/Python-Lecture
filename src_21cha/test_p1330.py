import pytest
from p1330 import operate


@pytest.mark.parametrize(
    ("a, b, expected"),
    [
        (1, 2, "<"),
        (3, 1, ">"),
        (5, 5, "=="),
    ],
)
def test_operate(a, b, expected):

    assert operate(a, b) == expected
