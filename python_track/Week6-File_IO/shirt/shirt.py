#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Problem 4: CS50 P-Shirt

Description: Implement a program that expects exactly two command-line arguments:
             - in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
             - in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
             The program should then overlay shirt.png (which has a transparent background) on the input after resizing and cropping the input to be the same size,
             saving the result as its output.
             The program should instead exit via "sys.exit":
              - if the user does not specify exactly two command-line arguments,
              - if the input’s and output’s names do not end in ".jpg", ".jpeg", or ".png", case-insensitively,
              - if the input’s name does not have the same extension as the output’s name, or
              - if the specified input does not exist.
             Assume that the input will be a photo of someone posing in just the right way, like these `demos`,
             so that, when they’re resized and cropped, the shirt appears to fit perfectly.
"""


from PIL import Image, ImageOps
import os
import sys


def main():
    """run image interposing program"""
    error_checks()
    image1 = sys.argv[1]
    image2 = sys.argv[2]
    interpose(image1, image2)


def error_checks():
    """error checker for command-line arguments"""
    if len(sys.argv) <= 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        path_1 = os.path.splitext(sys.argv[1])
        path_2 = os.path.splitext(sys.argv[2])

        if path_1[1].lower() not in [".jpg", ".jpeg", ".png"] or path_2[
            1
        ].lower() not in [".jpg", ".jpeg", ".png"]:
            sys.exit("Invalid output")
        elif path_1[1].lower() != path_2[1].lower():
            sys.exit("Input and output have different extensions")


def interpose(image1, image2):
    """fit one image unto another image of similar dimensions"""
    size = (600, 600)
    try:
        with Image.open(image1) as im:
            image1_resize = ImageOps.fit(
                im, size, method=Image.BICUBIC, bleed=0.0, centering=(0.5, 0.5)
            )
        with Image.open("shirt.png") as shirt:
            # create new image
            shirt_resized = shirt.resize(image1_resize.size)
            # interpose new image on image1
            image1_resize.paste(shirt_resized, (0, 0), shirt_resized)
            image1_resize.save(image2)
    except FileNotFoundError:
        sys.exit("Input does not exist")
    except ValueError:
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
