"""
Author: Joshua Ampofo Yentumi

Problem 5: Tip Calculator

Description: Complete the implementation of two functions in the Tip calculator program.
             dollars_to_float: accepts a str as input, remove the leading $, and return the amount as a float.
             percent_to_float: accepts a str as input, remove the trailing %, and return the percentage as a float.
"""


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d[1:])


def percent_to_float(p):
    # obtain last two strings
    split_p = p[:2]
    # convert string to float
    float_p = float(split_p)
    # convert to decimal
    return float_p / 100


if __name__ == '__main__':
    main()
