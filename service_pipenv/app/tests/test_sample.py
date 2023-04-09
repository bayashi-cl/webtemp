import pytest

from util.func import add


@pytest.mark.parametrize(
    ("a", "b"),
    [
        (1, 2),
        (-1, 1),
    ],
)
def test_add(a: int, b: int) -> None:
    assert add(a, b) == a + b
