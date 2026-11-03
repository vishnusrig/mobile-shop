
from calculator import calculate_total, calculate_discounted_total


def test_total():
    assert calculate_total(15000, 500) == 15500


def test_discounted_total():
    assert calculate_discounted_total(15000, 500) == 14000
  
