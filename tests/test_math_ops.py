from src.matth_ops import mul, div
import pytest

def test_mul():
    assert mul(2, 3) == 6
    assert mul(-1, 5) == -5

def test_div():
    assert div(10,2) == 5
    with pytest.raises(ValueError):
        div(10,0)


