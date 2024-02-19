"""
Author: Joshua Ampofo Yentumi

PROBLEM SET 5

Problem 1: Testing my twttr

Description: Implement one or more functions that collectively test the implementation
             of "shorten" thoroughly, each of whose names should begin with "test_" 
             so that tests can be executed with:
             "pytest test_twttr.py.
"""

from twttr import shorten
import pytest


def test_argument_uppercase():
    """Test if function returns str in uppercase without vowels"""
    assert shorten("MADAM") == "MDM"
    assert shorten("MEDICINE") == "MDCN"
    assert shorten("TWITTER") == "TWTTR"


def test_argument_lowercase():
    """Test if function returns str in lowercase without vowels"""
    assert shorten("twitter") == "twttr"
    assert shorten("medicine") == "mdcn"
    assert shorten("jobs") == "jbs"


def test_argument_mixed_case():
    """Test if function returns str in mixed case without vowels"""
    assert shorten("twiTTeR") == "twTTR"
    assert shorten("MaNdAriN") == "MNdrN"


def test_longer_str():
    """Test if function can return longer strings without vowels"""
    assert shorten("Hello World") == "Hll Wrld"
    assert shorten("hello world") == "hll wrld"
    assert shorten("i love python") == " lv pythn"


def test_single_character():
    """Test if function can handle string with only one character"""
    assert shorten("a") == ""
    assert shorten("d") == "d"


def test_vowels_only():
    """Test if function can handle only vowels"""
    assert shorten("aeiou") == ""


def test_full_alphabet():
    """Test if function can handle full alphabet"""
    assert shorten("abcdefghijklmnopqrstuvwxyz") == "bcdfghjklmnpqrstvwxyz"


def test_empty_string():
    """Test if function returns an empty string when given an empty string"""
    assert shorten("") == ""


def test_numbers():
    """Test if function raises a TypeError when numbers or symbols are entered"""
    with pytest.raises(ValueError):
        shorten("1234")