#!/usr/bin/env python3
"""
Author: Joshua Ampofo Yentumi

PROBLEM SET 7
Problem 1: Implement a function called `validate` that expects an IPv4 address as input
           as a 'str' and then returns "True" or "False", respectively, if that input is
           a valid IPV4 address or not.
           
           You may not import any other libraries apart from "re".
"""


import re


def main():
    """run validate program"""
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    """runs validitiy checks on a str input as an IPv4 address

    Arg(s):
        ip (str): IPv4 input from user

    Returns:
        True if address is valid else False
    """
    match = re.search(
        r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$",
        ip,
    )
    return True if match else False


if __name__ == "__main__":
    main()
