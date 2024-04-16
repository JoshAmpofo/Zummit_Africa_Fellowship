#!/usr/bin/env python3

def file_opener(file):
    with open(file, "r") as file:
        for line in file:
            return line.strip()
    