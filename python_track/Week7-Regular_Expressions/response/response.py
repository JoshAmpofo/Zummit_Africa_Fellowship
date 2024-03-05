#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Problem 5: Response Validation

Description: Using either `validator-collection` or `validators` from PyPI, implement a program that prompts the user for an email address 
             via input and then prints "Valid" or "Invalid", respectively, if the input is a syntatically valid email address. 
             You may not use `re`. And do not validate whether the email address's domain name actually exists.
"""


from validator_collection import validators, errors


def main():
    """run email validation program"""
    print(validate_email(input("What's your eamil address? ").strip()))


def validate_email(email):
    """
    Validate an email address
    
    Arg(s):
        email (str): input email to validate
    
    Results:
        str: Valid or Invalid
    """
    try:
        if validators.email(email):
            return "Valid"
    except (ValueError, errors.InvalidEmailError):
        return "Invalid"
    

if __name__ == "__main__":
    main()