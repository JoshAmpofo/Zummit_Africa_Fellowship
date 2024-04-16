import pyttsx3
import docx
import sys

engine = pyttsx3.init()
filepath = sys.argv[1]

doc = docx.Document(filepath)
fullText = []
try:
    for paragraph in doc.paragraphs:
        fullText.append(paragraph.text)
        words = '\n'.join(fullText)
    engine.say(words)
    engine.runAndWait()
except FileNotFoundError:
    print("File not found")
except TypeError:
    print("File not a docx file")