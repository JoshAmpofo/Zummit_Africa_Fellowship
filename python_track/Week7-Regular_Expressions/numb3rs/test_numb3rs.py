#!/usr/bin/env python3
"""
Author: Joshua Ampofo Yentumi

Problem 1: Tests for Numb3rs.py
"""

from numb3rs import validate


def test_correct_ip():
    """Test if function can correclt validate right IPv4 addresses"""
    assert validate("192.168.0.1") == True
    assert validate("10.0.0.1") == True
    assert validate("172.16.0.1") == True
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("19.117.63.126") == True
    assert validate("255.255.253.0") == True


def test_incorrect_ip():
    """Test if function can correctly flag wrong IPv4 addresses"""
    assert validate("256.168.0.1") == False
    assert validate("192.168.0.300") == False
    assert validate("192.168.1") == False
    assert validate("192.168.0.0/24") == False


def test_mix_ip():
    """Test if function can correctly flag mixed character IPv4 addresses"""
    assert validate("1a2.125.125.125") == False
    assert validate("a12.127.127.127") == False
    assert validate("127.1b2.127.127") == False
    assert validate("127.127.1A7.127") == False
    assert validate("255.255.255.2B5") == False


def test_non_numeric_ip():
    """Test if function can correctly flag non numeric IPv4 addresses"""
    assert validate("cat") == False
    assert validate("dog.cat.mouse.rat") == False
    assert validate("CAT.DOG.MOUSE.RAT") == False
