#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Problem 3: Scourgify

Description: implement a program that expects the user to provide two command-line arguments:
             - the name of an existing CSV file to read as input, whose columns are assumed to be, in order: "name" and "house", and
             - the name of a new CSV to write as output, whose columns should be, in order: "first", "last", and "house".
             - Converts that input to that output, splitting each name into a first name and last name.
               Assume that each student will have both a first name and last name.
            If the user does not provide exactly two command-line arguments, or if the first cannot be read,
            the program should exit via `sys.exit` with an error message.
"""


import csv
import sys


def main():
    """run CSV data cleaning program"""
    error_checks()
    unclean_data = sys.argv[1]
    clean_data = sys.argv[2]
    data = read_data(unclean_data)
    write_data(clean_data, data)


def error_checks():
    """run error checks on command-line arguments"""
    if len(sys.argv) <= 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[0].endswith(".csv") or not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")


def read_data(unclean_data):
    """read unformatted data from CSV file"""
    names = []
    try:
        # read unformatted data
        with open(unclean_data, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"].split(", ")
                first, last, house = name[1], name[0], row["house"]
                names.append({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {unclean_data}")
    return names


def write_data(clean_data, data):
    # write formatted data to new csv file
    try:
        with open(clean_data, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for info in data:
                writer.writerow(info)
    except FileNotFoundError:
        sys.exit(f"Could not write to {clean_data}")


if __name__ == "__main__":
    main()
