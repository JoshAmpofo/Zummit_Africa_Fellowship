#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Description: A simple file reader that reads txt, pdf, and doc files 
"""


from pypdf import PdfReader
import docx
from controls import FileReaderControls
import pyttsx3
import argparse

engine = pyttsx3.init()


def main():
    """
    run file reader program
    """
    # instantiate controls
    file_reader_controls = FileReaderControls()

    # create argument parser
    parser = argparse.ArgumentParser(
        description="A simple text-to-speech program that can read pdfs, text files and word documents"
    )
    parser.add_argument("filepath", type=str, help="path to file to read")
    parser.add_argument(
        "-v",
        "--volume",
        type=int,
        default=25,
        help="volume level of reader engine(0-100)",
    )
    parser.add_argument(
        "-r",
        "--rate",
        type=int,
        default=20,
        help="speech rate or speed of reader engine (0-100)",
    )
    parser.add_argument(
        "-v-id",
        "--voice",
        type=int,
        default=0,
        help="Voice type/id of TTS engine (0 for male, 1 for female)",
    )

    args = parser.parse_args()

    # parse arguments to respective function parameters
    filepath = args.filepath
    volume = args.volume
    rate = args.rate
    voice = args.voice

    # call class functions on argparse arguments
    file_reader_controls.setVolume(volume)
    file_reader_controls.setRate(rate)
    file_reader_controls.setVoice(voice)

    # run on appropriate files
    if not (filepath.endswith('.txt') or filepath.endswith('.pdf') or filepath.endswith('.docx')):
        raise ValueError("Invalid file type. Valid file types are: .txt, .pdf, .docx")
    
    try:
        if filepath.endswith(".txt"):
            txtFile(filepath, volume, rate, voice)
        elif filepath.endswith(".pdf"):
            pdfFile(filepath, volume, rate, voice)
        elif filepath.endswith(".docx"):
            docFile(filepath, volume, rate, voice)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f'Error: {e}')


def txtFile(filepath, volume=25, rate=20, voice=0):
    """
    read a txt file

    Arg(s):
        filepath (str): path to file to read
        volume (int): default volume of TTS engine
        rate (int): default speech rate of TTS engine
        voice (int): default voice id of TTS engine
    """
    try:
        with open(filepath) as file:
            for line in file:
                engine.say(line.strip())
                engine.runAndWait()
    except FileNotFoundError:
        raise FileNotFoundError("File not found")
    except Exception as e:
        return f"Error: {e}"


def pdfFile(filepath, volume=25, rate=20, voice=0):
    """
    read pdf file

    Arg(s):
        filepath (str): path to file to read
        volume (int): default volume of TTS engine
        rate (int): default speech rate of TTS engine
        voice (int): default voice id of TTS engine
    """
    try:
        reader = PdfReader(filepath)
        for page in reader.pages:
            extracted_text = page.extract_text(
                extraction_mode="layout", layout_mode_scale_weight=1.0
            )
            engine.say(extracted_text)
            engine.runAndWait()
    except FileNotFoundError:
        raise FileNotFoundError("File not found")
    except Exception as e:
        print(f"Error: {e}")


def docFile(filepath, volume=25, rate=20, voice=0):
    """
    read a word doc file

    Arg(s):
        filepath (str): path to file to read
        volume (int): default volume of TTS engine
        rate (int): default speech rate of TTS engine
        voice (int): default voice id of TTS engine
    """
    try:
        doc = docx.Document(filepath)
        fullText = []
        for paragraph in doc.paragraphs:
            fullText.append(paragraph.text)
            words = "\n".join(fullText)
        engine.say(words)
        engine.runAndWait()
    except FileNotFoundError:
        raise FileNotFoundError("File not found")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
