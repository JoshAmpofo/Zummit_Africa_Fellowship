#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Problem 3: Adieu, Adieu

Description: Implement a program that prompts the user for names, one per line, until the user inputs "CTRL+D".
             Assume that the user will input at least one name. Then bid adieu to those names,
             separating two names with one "and", three names with two commas, and one "and",
             and n names with n - 1 commas and one "and", as in the below:

             Adieu, adieu, to Liesl
             Adieu, adieu, to Liesl and Friedrich
             Adieu, adieu, to Liesl, Friedrich, and Louisa
             Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
             Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
             Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
             Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
"""


import inflect
import sys

# instantiate inflect engine
p = inflect.engine()



def punctuate():
    """
    Grammatically punctuate a list of names inputted by user and bid Adieu to names
    """
    # create a names list to store inputs from user
    names = []
    while True:
        try:
            name = input("Name: ").strip()
            names.append(name)
        except EOFError:
            print("\nAdieu, adieu, to", p.join(names))
            sys.exit(0)


if __name__ == "__main__":
    punctuate()
