from pypdf import PdfReader
import pyttsx3
import sys


filepath = sys.argv[1]
engine = pyttsx3.init()
reader = PdfReader(filepath)

try:
    for page in reader.pages:
        engine.say(page.extract_text(extraction_mode="layout", 
                                 layout_mode_space_vertically=False))
        engine.runAndWait()
except FileNotFoundError:
    print("File does not exist")
except TypeError:
    print("File not a pdf")