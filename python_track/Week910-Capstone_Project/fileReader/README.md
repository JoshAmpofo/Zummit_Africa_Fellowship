# Simple File Reader :files:

## Video Demo: <#URL HERE>

### Synopsis

Reading is an essential skill for a developer. It helps you improve your knowledge as well as stay up to date with happenings around you.
However, the hustle and bustle of everyday living can result in not having time to read. To solve this challenge, the *file_reader* program was developed.

## Table of Contents

- [**Description**](#description)
- [**Installation**](#installation)
- [**Usage**](#usage)
- [**Supported File Types**](#supported-file-types)
- [**Controls**](#controls)
- [**Contributing**](#contributing)
- [**Testing**](#testing)

## Description

This is a simple command-line program that can read PDF, text, and Word document files. It utilizes the Python libraries **pypdf**, **docx**, and **pyttsx3** for reading PDFs, Word documents, and converting text to speech, respectively. The main program can be found in the **file_reader.py** file.

Helper functions like the reader controls that allow the user to adjust the *volume*, choose the *speed rate* of the reader as well as the *voice* to use, can be found in the **controls.py** file.

Tests for the robustness and correctness of the program can be found in the **test_filereader.py** file.

Dependencies required for the program to run successfully can be found in the **requirements.txt** file.

In choosing the text-to-speech (TTS) engine to use, the python module *pyttsx3* was chosen due to its simplicity of use and availability for offline use. Thus users can use the program with or without connecting to the internet.

Going forward, additional functionality will be added to enhance the reading experience of the user such as OCR recognition, customizable hotkeys, text summarization, text-to-speech markup support, automatic language detection together with a nice user interface (UI).

## Installation

To use the **file_reader** program, follow these steps:

- Clone this repository to your local machine:
`git clone https://github.com/JoshAmpofo/Zummit_Africa_Fellowship/python_track/Week910-Capstone_Project/fileReader.git`

- Install the required dependencies:
`pip install -r requirements.txt`

## Usage

After installation, you can run the program using the following command:

`python file_reader.py <file_path> <options>`

- Replace <file_path> with the path to the file you want to read. Additionally, you can specify optional parameters:
  - **volume**: Adjust the volume of the speech (0-100).
  - **rate**: Adjust the speech rate (0-100).
  - **voice**: Select a voice for speech synthesis (currently supports only two voices: male[id=0] and female[id=1]).

`For example:`
`python file_reader.py example.pdf --volume=70 --rate=80 --voice=1`

- The program will run successfully even without specifying any additional options. The default settings will be used in this case
`For example:`
`python file_reader.py <file_path>`

## Supported File Types

- The program supports the following file types:
  - *PDF*: Use **.pdf** files.
  - *Text*: Use **.txt** files.
  - *Word Document*: Use **.docx** files.

## Controls

The [**controls.py**](controls.py) file provides additional functionality to control the reading experience. You can adjust the volume, speech rate, and select different voices for speech synthesis.

## Contributing

- While I'll do my best to improve the functionality of this program, contributions are welcome! If you'd like to contribute to this project, please follow these steps:
  - **Fork the repository**.
  - **Create a new branch (git checkout -b feature/new-feature).**
  - **Make your changes.**
  - **Commit your changes (git commit -am 'Add new feature').**
  - **Push to the branch (git push origin feature/new-feature).**
  - **Create a new Pull Request.**

## Testing

- Several tests were written to check the robustness, correctness and reproducibility of this program.
These tests can be found here [**Tests**](test_filereader.py).
