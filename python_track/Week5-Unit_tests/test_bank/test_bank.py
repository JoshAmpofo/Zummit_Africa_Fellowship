"""
Author: Joshua Ampofo Yentumi

Problem 2: Tests for Back to the Bank

Description: Re-implement Home Federal Savings Bank from Problem Set 1.
             restructuring the code per the below, wherein ```value``` expects a ```str``` as input and returns
             an ```int```, namely 0 if that str starts with "hello", 20 if that str starts with an "h" (but not "hello"),
             or 100 otherwise, treating the str case-insentively.
             Assume that the string passed to the ```value``` function will not contain any leading spaces.
             Only "main" should call ```print```
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


def test_greeting_not_a_str():
    """Test if function raises an error when greeting is not a str"""
    with pytest.raises(AttributeError):
        value(12345)

