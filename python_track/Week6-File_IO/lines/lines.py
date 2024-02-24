#!/usr/bin/env python3
"""
Author: Joshua Ampofo Yentumi

PROBLEMS SET 6

Problem 1: Lines of Code

Description: Implement a program that expects exactly one command-line argument, the name (or path) of a Python file,
             and outputs the number of lines of code in that file, excluding comments and blank lines.
             If the user does not specify exactly one command-line argument, or if the specified file's name does not end in ".py",
             or if the specified file does not exist, the program should instead exit via "sys.exit".

             Assume that any line that starts with "#", optionally preceded by whitespace, is a comment.
             A docstring should not be considered a comment.
             Assume that any line that only contains whitespace is blank.
"""


import sys


def main():
    """run count_lines program"""
    # error checks
    error_checks()

    # run main program
    filename = sys.argv[1]
    print(count_lines(filename))


def error_checks():
    """perform error checks on command line arguments"""
    if len(sys.argv) <= 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")


def count_lines(filename):
    """count the number of lines in a file"""
    try:
        with open(filename, "r") as file:
            # set counter
            line_count = 0
            for line in file:
                # check if line is not a comment or blank space
                if not line.lstrip().startswith("#") and line.strip():
                    line_count += 1
            return line_count
    except FileNotFoundError:
        return "File does not exist"


if __name__ == "__main__":
    main()
