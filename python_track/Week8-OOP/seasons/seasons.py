#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi
PROBLEM SET 8

Problem 1: Seasons of Love

Description: Implement a program that prompts the user for their date of birth in "YYYY-MM-DD" format
             and then prints how old they are in "minutes", rounded to the nearest integer,
             using English words instead of numerals, just like the song from Rent, without any "and" between words.

             For simplicity assume that the user was born at midnight (i.e. 00:00:00) on that date.
             Assume that the current time is also midnight, even if the user runs the program at noon, assume that it's actually midnight on the same date.
             Use `datetime.date.today` to get today's date
"""

from datetime import datetime, date
import inflect
import sys

p = inflect.engine()


class Age:
    """creates a class that converts age to minutes"""

    def __init__(self, dob):
        try:
            self.dob = datetime.strptime(dob, "%Y-%m-%d").date()
        except ValueError:
            sys.exit("Invalid date")

    def __sub__(self, other):
        return other.dob.year - self.dob.year

    def age_in_minutes(self):
        today = date.today()
        age_in_minutes = (today - self.dob).total_seconds() // 60
        return round(age_in_minutes)


def main():
    """run the age in minutes program"""
    dob = input("Date of Birth: ")
    age = Age(dob)
    age_minutes = age.age_in_minutes()
    print(f"{p.number_to_words(age_minutes, andword='').capitalize()} minutes")


if __name__ == "__main__":
    main()
