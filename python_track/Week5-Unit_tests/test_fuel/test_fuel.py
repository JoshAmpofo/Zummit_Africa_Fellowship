"""
Author: Joshua Ampofo Yentumi

Problem 4: Tests for Refueling
"""

import pytest
from fuel import convert, gauge


def test_valid_fraction_string():
    """Test if function returns the correct percentage when given a valid fraction string in the format X/Y."""
    assert convert("3/4") == 75


def test_round_nearest_integer():
    """Test if function rounds the percentage to the nearest integer."""
    assert convert("3/4") == 75


def test_return_zero():
    """Test if function returns 0 when given the fraction string "0/1"."""
    assert convert("0/1") == 0


def test_return_one_hundred():
    """Test if function returns 100 when given the fraction string "1/1"."""
    assert convert("1/1") == 100


def test_returns_50():
    """Test function returns 50 when given the fraction string "1/2"."""
    assert convert("1/2") == 50


def test_returns_33():
    """Test function returns 33 when given the fraction string "1/3"."""
    assert convert("1/3") == 33


def test_returns_25():
    """Test function returns 25 when given the fraction string "1/4"""
    assert convert("1/4") == 25


def test_raises_zero_division_error():
    """Test that function raises a ZeroDivisionError"""
    with pytest.raises(ZeroDivisionError):
        convert("0/0")


def test_x_greater_than_y():
    """Test if function raises a ValueError when X is greater than Y."""
    with pytest.raises(ValueError):
        convert("5/2")


def test_percentage_less_than_or_equal_to_1():
    """Test if function returns "E" if percentage is less than or equal to 1"""
    assert gauge(1) == "E"


def test_percentage_greater_than_or_equal_to_99():
    """Test if function returns "F" if percentage is greater than or equal to 99"""
    assert gauge(99) == "F"


def test_percentage_between_1_and_99():
    """Test if function returns formatted percentage string if percentage is between 1 and 99"""
    assert gauge(50) == "50%"


def test_negative_percentage():
    """Test function returns "E" if percentage is negative"""
    assert gauge(-10) == "E"
    assert gauge(-5) == "E"


def test_percentage_greater_than_100():
    """Test function returns "F" if percentage is greater than 100"""
    assert gauge(110) == "F"
    assert gauge(200) == "F"
