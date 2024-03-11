#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Problem 2: Tests for Cookie Jar
"""

from jar import Jar
import pytest


class TestJar:

    def test_init(self):
        """Test class initialization method"""
        cookie_object = Jar()
        assert cookie_object.capacity == 12
        cookie_object_2 = Jar(10)
        assert cookie_object_2.capacity == 10

    def test_str(self):
        """Test if function can add specified number of cookies and return as str"""
        jar = Jar()
        assert str(jar) == ""
        jar.deposit(10)
        assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
        jar.deposit(1)
        assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
        

    def test_deposit(self):
        """Test if deposit function can add correct number of cookies"""
        jar = Jar()
        jar.deposit(5)
        assert jar.size == 5
        jar_2 = Jar()
        jar_2.deposit(10)
        assert jar_2.size == 10
        jar_3 = Jar()
        jar_3.deposit(2)
        assert jar_3.size == 2
        with pytest.raises(ValueError):
            jar.deposit(-5)
            jar.deposit(15)
            jar.deposit("cat")

    def test_withdraw_with_enough_cookies(self):
        """Test if function can remove cookies from jar when enough available"""
        jar = Jar()
        jar.deposit(10)
        jar.withdraw(5)
        assert jar.size == 5

    def test_withdraw_from_empty_jar(self):
        """Test if function raises ValueError when withdrawing from empty jar"""
        jar = Jar()
        with pytest.raises(ValueError):
            jar.withdraw(5)

    def test_withdraw_non_int_type(self):
        """Test if function raises ValueError when value is a non-negative int or not an int"""
        jar = Jar()
        with pytest.raises(ValueError):
            jar.withdraw("Cat")
            jar.withdraw(-5)
