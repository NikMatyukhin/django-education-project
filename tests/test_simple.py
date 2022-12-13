import pytest


def absolute(a):
    if a < 0:
        return -a
    return a


@pytest.mark.parametrize(["args", "expected"], [[-1, 1], [0, 0], [1, 1]])
def test_absolute(args, expected):
    assert absolute(args) == expected
