"""
Author: Joshua Ampofo Yentumi

Problem 4: Refueling

Description: Reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:
             `convert` expects a str in `X/Y` format as input, wherein each of X and Y is an integer,
             and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive.
             If X and/or Y is not an integer, or if X is greater than Y, then `convert` should raise a 'ValueError'.
             If Y is 0, then `convert` should raise a 'ZeroDivisionError'.
             `gauge` expects an int and returns a str that is:
                - "E" if that int is less than or equal to 1,
                - "F" if that int is greater than or equal to 99, and
                - "Z%" otherwise, wherein Z is that same int.
"""


def main():
    """run refueling function"""
    fraction = input("Fraction: ")
    print(gauge(convert(fraction)))


def convert(fraction):
    """returns a string in the format X/Y as a percentage rounded to the nearest int"""
    x, y = map(int, fraction.split("/"))

    if x > y:
        raise ValueError

    if y == 0:
        raise ZeroDivisionError

    frac = x / y
    percentage = round(frac * 100)
    return percentage


def gauge(percentage):
    """Prints out the fuel percentage level"""
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
