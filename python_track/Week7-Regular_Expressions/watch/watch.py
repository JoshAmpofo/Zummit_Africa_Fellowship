#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Problem 2: Watch on YouTube

Description: Implement a function called `parse` that expects a str of HTML as input, extracts any YouTube URL that's the value of a src attribute 
             of an iframe element therein, and returns its shorter, shareable youtu.be equivalent as a str. 
             Expect that any such URL will be in one of the formats below: 
                - http://youtube.com/embed/xvFZjo5PgG0
                - https://youtube.com/embed/xvFZjo5PgG0
                - https://www.youtube.com/embed/xvFZjo5PgG0
             Assume that the value of src will be surrounded by double quotes. And assume that the input will contain no more than one such URL. 
             If the input does not contain any such URL at all, return "None".
"""


import re


def main():
    """run HTML parse program"""
    print(parse(input("HTML: ").strip()))


def parse(s):
    """convert a youtube URL into a shorter shareable URL

    Arg:
        s (str): long youtube URL to shorten

    Returns:
        (str): shortened shareable youtube URL
    """
    if match := re.search(r"src=\"(.*?embed.*?)\"", s, re.IGNORECASE):
        split_url = match.group(1).split("/")
        short_url = "https://youtu.be/" + split_url[4]
        return short_url
    else:
        return None


if __name__ == "__main__":
    main()
