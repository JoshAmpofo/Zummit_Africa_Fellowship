#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Problem 4: Tests for Regular, um, Expressions
"""


from um import count


def test_count_multitext():
    """Test if function correctly counts um in long text"""
    assert count("Hi, My name is, um, Joshua") == 1
    assert count("Beautiful people, um, are every, um where") == 2
    assert count("um, let's be, um, very good, um, friends") == 3
    assert count("um..., hello everyone") == 1
    assert count("You need to leave me um, alone here") == 1


def test_count_shorttext():
    """Test if function correctly counts um in short text"""
    assert count("um...") == 1
    assert count("um, um, um") == 3
    assert count("lol, um") == 1


def test_count_no_ums():
    """Test if function returns 0 when no um in text"""
    assert count("cat") == 0
    assert count("dogum") == 0
    assert count("umpire") == 0
    assert count("yummy") == 0


def test_count_uppercase():
    """Test if function can correctly count str ignoring case"""
    assert count("UM") == 1
    assert count("hello, UM, my name is Peabody") == 1
    assert count("YUMMY") == 0
    assert count("UM...") == 1
    assert count("Tomorrow is a UM, a beautiful day") == 1
    assert count("NOTHING IS UM ALRIGHT!") == 1
