#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Problem 2: Pizza Py

Description: Implement a program that expects exactly one command-line argument - the name (or path) of a CSV file
             in Pinocchio's format, and outputs a table formatted as ASCII art using `tabulate`.
             Format the table using the library's `grid` format.
             If the user does not speecify exactly one command-line argument, or if the specified file's name does not
             end in `.csv`, or if the specified file does not exist, the program should instead exit via `sys.exit`
"""

import csv
import sys
from tabulate import tabulate


def main():
    """run Pizza Py program"""
    error_checks()
    filename = sys.argv[1]
    print(pizza_py(filename))


def error_checks():
    """run file validation checks on command-line input"""
    if len(sys.argv) <= 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")


def pizza_py(filename):
    """format pizza prices of Pinocchios in ASCII art"""
    try:
        with open(filename) as file:
            reader = csv.reader(file)
            data = list(reader)
            return tabulate(data[1:], headers=data[0], tablefmt="grid")
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
