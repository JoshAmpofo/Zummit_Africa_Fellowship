#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Problem 3: CS50 Shirtificate

Description: Implement a program that prompts the user for their name and outputs, using "fpdf2",
             a CS50 shirtificate in a file called "shirtificate.pdf" with the ff specifications:
                - The orientation of the PDF should be "Potrait"
                - The format of the PDF should be "A4" which is "210mm wide" by "297mm tall"
                - The top of the PDF should say "CS50 Shirtificate" as text, centered horizontally.
                - The user's name should be on top of the shirt, in white text.
            You are welcome to add any other details as you see fit.
"""
from fpdf import FPDF, Align


class Shirtificate(FPDF):
    """Create custom pdf shirt"""
    def header(self):
        """create pdf title header"""
        self.set_font("Helvetica", "", 50)
        self.cell(60, 50, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT",
                  align="C", center=True)
        
    def add_image(self, URL):
        """Add image to pdf"""
        self.image(URL, x=Align.C, y=60, dims=(540, 540))
        
    def add_text(self, text):
        """Add text to fron of shirt"""
        self.set_font("Helvetica", "", 25)
        self.set_text_color(255, 255, 255)
        self.set_xy(0, 100)
        self.cell(0, 50, text, align='C', center=True)
        
        

def main():
    """run CS50 shirtificate program"""
    name = input("Name: ")
    URL = "D:/Machine_Learning/Zummit Africa Fellowship/classes/Zummit_Africa_Fellowship/python_track/Week8-OOP/shirtificate/shirtificate.png"
    print_image(name, URL)
    
def print_image(name, URL):
    """Print shirtificate"""
    pdf = Shirtificate()
    pdf.add_page() # create page
    pdf.add_image(URL) # add image
    pdf.add_text(name + " took CS50")
    pdf.output("Shirtificate_2.pdf") # output
    

if __name__ == "__main__":
    main()