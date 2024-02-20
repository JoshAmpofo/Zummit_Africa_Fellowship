"""
Author: Joshua Ampofo Yentumi

Problem 3: Tests for Vanity Plates
"""

import pytest
from plates import is_valid


def test_only_letters_length_between_2_and_6():
    """Test if input string with only letters and length between 2 and 6 returns True"""
    assert is_valid("abc") == True
    assert is_valid("abcdef") == True
    assert is_valid("a") == False
    assert is_valid("abcdefghi") == False
    assert is_valid("123") == False
    assert is_valid("abc123") == True


def test_only_numbers_length_between_2_and_6():
    """Test if input string with only numbers and length between 2 and 6 returns True"""
    assert is_valid("123") == False
    assert is_valid("123456") == False
    assert is_valid("1") == False
    assert is_valid("1234567") == False
    assert is_valid("abc") == True
    assert is_valid("abc123") == True


def test_letters_and_numbers_start_with_2_letters_end_with_numbers():
    """Test if input string with letters and numbers, starting with at least 2 letters and ending with numbers, returns True"""
    assert is_valid("ab12") == True
    assert is_valid("abc123") == True
    assert is_valid("a1") == False
    assert is_valid("123abc") == False
    assert is_valid("abc") == True
    assert is_valid("123") == False


def test_length_less_than_2():
    """Test if input string with length less than 2 returns False"""
    assert is_valid("") == False
    assert is_valid("a") == False
    assert is_valid("1") == False
    assert is_valid(" ") == False
    assert is_valid("!") == False
    assert is_valid("@") == False


def test_length_greater_than_6():
    """Test if input string with length greater than 6 returns False"""
    assert is_valid("abcdefg") == False
    assert is_valid("1234567") == False
    assert is_valid("abcdefghi") == False
    assert is_valid("123456789") == False
    assert is_valid("abc123def") == False
    assert is_valid("abc123def456") == False


def test_one_letter_one_number():
    """Test if input string with only one letter and one number returns False"""
    assert is_valid("a1") == False
    assert is_valid("b2") == False
    assert is_valid("c3") == False
    assert is_valid("d4") == False
    assert is_valid("e5") == False
    assert is_valid("f6") == False


def test_start_with_letters_not_end_with_numbers():
    """Test if input string with letters and numbers, starting with at least 2 letters and not ending with numbers, returns False"""
    assert is_valid("ab12ab") == False
    assert is_valid("abc123c") == False
    assert is_valid("a1b2c3") == False


def test_not_start_with_letters():
    """Test if input string with letters and numbers, not starting with at least 2 letters, returns False"""
    assert is_valid("1ab") == False
    assert is_valid("123abc") == False
    assert is_valid("12a3b4c") == False


def test_only_letters_end_with_zero_number():
    """Test if input string with only letters and ending with a number starting with 0 returns False"""
    assert is_valid("abc0") == False
    assert is_valid("abcd0") == False
    assert is_valid("abcde0") == False


def test_only_letters_ending_with_number():
    """Test if input string with only letters and ending with a number not starting with 0 returns True"""
    assert is_valid("abc1") == True
    assert is_valid("abcdef2") == False
    assert is_valid("abc") == True
    assert is_valid("abcdef") == True
    assert is_valid("123") == False
    assert is_valid("abc123") == True


def test_only_numbers_ending_with_letter():
    """Test if input string with only numbers and ending with a letter returns False"""
    assert is_valid("123a") == False
    assert is_valid("456def") == False
    assert is_valid("123") == False
    assert is_valid("4567") == False
    assert is_valid("abc") == True
    assert is_valid("abc123") == True


def test_numbers_starting_with_zero():
    """Test if input string with only numbers and starting with 0 returns False"""
    assert is_valid("0123") == False
    assert is_valid("04567") == False
    assert is_valid("123") == False
    assert is_valid("4567") == False
    assert is_valid("abc") == True
    assert is_valid("abc123") == True


def test_alphanum():
    """Test function on alphanumerics"""
    assert is_valid("$!") == False
    assert is_valid("*ab22") == False
    assert is_valid(" AB22") == False
    assert is_valid("AB22  ") == False
    assert is_valid("#$") == False
