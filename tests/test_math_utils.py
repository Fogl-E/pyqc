import pytest
from src.pyqc import math_utils

def test_add():
    assert math_utils.add(2,3) == 5

def test_multiply():
    assert math_utils.multiply(2,3) == 6

def test_power():
    assert math_utils.power(2,3) == 8