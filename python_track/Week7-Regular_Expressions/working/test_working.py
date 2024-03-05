#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Problem 3: Tests for Working 9 to 5
"""

import pytest
from working import convert


def test_correct_time_formats():
    """Test if function returns correct 24hr format when given correct 12hr format"""
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 10:00 PM") == "09:00 to 22:00"
    assert convert("10 AM to 10 PM") == "10:00 to 22:00"
    assert convert("10:30 PM to 12:30 PM") == "22:30 to 12:30"
    assert convert("6 AM to 8 AM") == "06:00 to 08:00"
    assert convert("9 PM to 4 AM") == "21:00 to 04:00"
    assert convert("10:00 AM to 5:00 PM") == "10:00 to 17:00"
    assert convert("10:45 AM to 6:33 PM") == "10:45 to 18:33"


def test_wrong_time_format():
    """Test if function returns error message when time format is wrong"""
    with pytest.raises(ValueError):
        assert convert("9:60 AM - 12:60 PM")
        assert convert("9 AM - 10 AM")
        assert convert("9 PM - 12 PM")
        assert convert("9:00 AM to 10:60 AM")
        assert convert("9AM to 10AM")
        assert convert("9:00AM to 10:00AM")
        assert convert("9:00PM to 10:30PM")
        assert convert("AM:PM to PM:PM")
        assert convert("cat")
        assert convert("")

def test_out_of_range_times():
    with pytest.raises(ValueError):
        assert convert("99:00 AM to 85:00 PM")
        assert convert("85 AM to 95 AM")
        assert convert("85:00 PM to 99:00 AM")
        assert convert("85 PM to 90 PM")
        assert convert("23:00 AM to 24:00 PM")
        assert convert("24 AM to 23 PM")

