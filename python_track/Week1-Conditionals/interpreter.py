"""
Author: Joshua Ampofo Yentumi

Problem 4: Math Interpreter

Description: Implement a program that prompts the user for an arithmetic expression
             and then calculates and outputs the results as a floating-point value
             formatted to one decimal place.
             Assume that the user's input will be formatted as "x y z", with one space between x and y,
             and one space between y and z, wherein:
             x is an integer
             y is +, -, *, or /
             z is an integer
             Assume that, if y is /, then z will not be 0.
"""

expression = input("Expression: ")
expression = expression.split()


match expression:
    case [x, "+", z]:
        result = float(x) + float(z)
    case [x, "*", z]:
        result = float(x) * float(z)
    case [x, "-", z]:
        result = float(x) - float(z)
    case [x, "/", z]:
        result = float(x) / float(z)
    case _:
        print("Unknown expression")

if result:
    print(f"{result:.1f}")
