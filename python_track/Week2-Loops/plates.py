"""
Author: Joshua Ampofo Yentumi

Problem 4: Vanity Plates

Description: Implement a program that prompts a user for a vanity plate and then output "VALID"
             if meets all of the requirements or "INVALID" if it does not. Assume that any letters in the
             user's input will be uppercase. Structure your program per the below, wherein "is_valid" returns "True"
             if "s" meets all requirements and "False" if does not.
             Assume that "s" will be a str.

             Vanity Plate Requirements:
             - "All vanity plates must start with at least two letters"
             - "...vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters."
             - "Numbers cannot be used in the middle of a plate; they must come at the end.
                For example, AAA222 would be an acceptable vanity plate; AAA22A would not be acceptable.
                - The first number cannot be a 0.
            - "No periods, spaces, or punctuation marks are allowed"
"""


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """check if string fulfills all vanity plate requirements"""
    # Check length
    if not  (2 <= len(s) <= 6):
        return False

    # separate string into letters and numbers
    letters = ''.join([char for char in s if char.isalpha()])
    numbers = ''.join([num for num in s if num.isdigit()])

    # check if plate starts with at least letters
    if len(letters) < 2 or not s.startswith(letters):
        return False

    # check for only numbers at the end of plate and string does not start with 0
    if numbers:
        if not s.endswith(numbers) or numbers[0] == '0':
            return False

    # all conditions satisfied
    return True


if __name__ == '__main__':
    main()
