"""
Author: Joshua Ampofo Yentumi

Problem 2: Tests for Back to the Bank
"""


import pytest
from bank import value



def test_hello():
    """Test if function returns 0 when greeting starts with 'hello'"""
    assert value("hello") == 0
    assert value("hello world") == 0
    assert value("hello!") == 0


def test_start_with_h_hello():
    """Test if function returns 20 when greeting starts with "h" and is not 'hello'"""
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("howdy") == 20


def test_other_greeting():
    """Test if function returns 100 for all other greetings"""
    assert value("good morning") == 100
    assert value("good afternoon") == 100
    assert value("good evening") == 100


def test_case_insensitive():
    """Test if function returns appropriate amount regardless of string case"""
    assert value("Good Morning") == 100
    assert value("heLLo") == 0
    assert value("Hello") == 0
    assert value("Hey") == 20


def test_greeting_not_a_str():
    """Test if function raises an error when greeting is not a str"""
    with pytest.raises(AttributeError):
        value(12345)

