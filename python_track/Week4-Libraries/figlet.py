#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Problem 2: Frank, Ian and Glen's Letters (FIGlet)

Description: Implement a program that:
             - Expects zero or two command-line arguments:
                o Zero if the user would like to output text in a random font.
                o Two if the user would like to output texxt in a specific font,
                  in which case the first of the two should be "-f" or "--font", and
                  the second of the two should be the name of the font.
             - Prompts the user for a "str" of text.
             - Outputs that text in the desired font.
             - If the user provides two command-line arguments and the first is not "-f" or "--font",
             or the second is not the name of a font, then the program should exit via "sys.exit" with an error message.
"""

from pyfiglet import Figlet
import random
import sys

# create global figlet instance
figlet = Figlet()
# retrieve available figlet font list
font_list = figlet.getFonts()

def main():
  """Output a given text in FIGlet format"""
  if len(sys.argv) == 1:  # check if no font style is specified
    text = input("Enter text: ")
    print_text_in_font(text)

  # check if more than one cmd argument is given
  elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    if sys.argv[2] not in font_list:
      sys.exit("Invalid usage")
    text = input("Enter text: ")
    print_text_in_font(text, sys.argv[2]) # display text in specified figlet font

  else:
    sys.exit("Invalid usage") # if style invalid


def get_random_font():
  """Retrieve random font style from FIGlet format list"""
  return random.choice(font_list)


def print_text_in_font(text, font=None):
  """convert text to specified figlet font style"""
  if font is None:  # if sys.argv[1] is empty
    font = get_random_font()  # use random font style

  # set font if correct font sytle is specified
  figlet.setFont(font=font)
  print(figlet.renderText(text))


if __name__ == "__main__":
    main()
