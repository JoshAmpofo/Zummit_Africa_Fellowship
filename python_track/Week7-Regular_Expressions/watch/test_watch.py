#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Problem 2: Tests for Watch Youtube
"""

import pytest
from watch import parse


def test_correct_url():
    """Test if function can shorten url matching search pattern"""
    assert (
        parse(
            '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player"></iframe>'
        )
        == "https://youtu.be/xvFZjo5PgG0"
    )
    assert (
        parse('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>')
        == "https://youtu.be/xvFZjo5PgG0"
    )
    assert (
        parse(
            '<iframe width="560" height="315" src="https://www.youtube.com/embed/abcdefGhiZ1"></iframe>'
        )
        == "https://youtu.be/abcdefGhiZ1"
    )


def test_wrong_url():
    """Test if function returns None on url not matching search pattern"""
    assert (
        parse(
            '<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>'
        )
        == None
    )
    assert (
        parse(
            '<iframe width="360" height="210" src="https://chat.openai.com"></iframe>'
        )
        == None
    )
    assert (
        parse(
            '<iframe width="550" height="300" src="https://www.youtube.com/anyvideo"></iframe>'
        )
        == None
    )


def test_no_url_str():
    """Test if function returns None when given only non-URL strings"""
    assert parse("cat") == None
    assert parse("DOG") == None
    assert parse("cAtDoG") == None


def test_no_url_num():
    """Test if function raises an error when given only numbers"""
    with pytest.raises(TypeError):
        assert parse(1234)
