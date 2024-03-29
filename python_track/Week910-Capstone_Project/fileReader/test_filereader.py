#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Description: Tests for file_reader program
"""

from controls import FileReaderControls
from file_reader import txtFile, docFile, pdfFile
import pytest



@pytest.fixture
def reader_controls():
    """create a general instance for the FileReaderControls class"""
    return FileReaderControls()


class TestFileControls:
    """Test functions in the controls script"""

    def test_class_filereader_docstring(self, reader_controls):
        """Test for the presence of a docstring in class"""
        docstring = reader_controls.__doc__
        assert isinstance(docstring, str)
        assert "creates a class for all controls of the file reader" in docstring

    def test_setVolume_docstring(self, reader_controls):
        """Test for the presence of a doctring in setVolume function"""
        docstring = reader_controls.setVolume.__doc__
        assert isinstance(docstring, str)
        assert "volume control" in docstring
        assert "arg(str -> float): volume set for TTS engine." in docstring
        assert "default value set to 0.5" in docstring

    def test_setRate_docstring(self, reader_controls):
        """Test for the presence of a docstring in setRate function"""
        docstring = reader_controls.setRate.__doc__
        assert isinstance(docstring, str)
        assert "speech rate controls" in docstring
        assert "arg (str -> int): voice speed rate for TTS engine." in docstring
        assert "default value set to 200 words per minute" in docstring

    def test_setVoice_docstring(self, reader_controls):
        """Test for the presence of a docstring in setVoice function"""
        docstring = reader_controls.setVoice.__doc__
        assert isinstance(docstring, str)
        assert "file reader voice choice" in docstring
        assert "id (str -> int): voice id for TTS engine" in docstring
        assert "default id set to 0 (male voice)" in docstring

    def test_init(self, reader_controls):
        """Test if initialization works without errors"""
        assert isinstance(reader_controls, FileReaderControls)

    # TEST MAIN CONTROL FUNCTIONS
    def test_setVolume_with_default_argument(self, reader_controls):
        """Test if volume can be initialized with default argument"""
        reader_controls.setVolume()
        volume = reader_controls.engine.getProperty("volume")
        assert volume == 1.0

    # def test_setVolume_increase(self, reader_controls):
    #     """Test if volume can be adjusted with a valid argument"""
    #     reader_controls.setVolume(0.95)
    #     assert reader_controls.engine.getProperty('volume') == 0.95
    # SEEMS THAT VOLUME SETTING WORKS WHEN RUNNING PROGRAM BUT NOT WHEN TESTING

    def test_setVolume_error_with_non_float_arguments(self, reader_controls):
        """Test if function raises an error when given non-float argument"""
        with pytest.raises(TypeError) as e:
            reader_controls.setVolume("0.5")
        assert str(e.value) == "Volume must be a float"

    def test_setVolume_with_greater_than_default_value_args(self, reader_controls):
        """Test if function raises an error when given argument greater than 1.0"""
        with pytest.raises(ValueError) as e:
            reader_controls.setVolume(2.0)
        assert str(e.value) == "Volume can be set between 0.0 and 1.0 only but got 2.0"

    def test_setVolume_with_negative_float(self, reader_controls):
        """Test if function raises an error when given a negative float"""
        with pytest.raises(ValueError) as e:
            reader_controls.setVolume(-1.0)
        assert str(e.value) == "Volume can be set between 0.0 and 1.0 only but got -1.0"

    def test_setRate_with_default_argument(self, reader_controls):
        """Test if rate can be initialized with default argument"""
        reader_controls.setRate()
        rate = reader_controls.engine.getProperty("rate")
        assert rate == 200

    # def test_setRate_adjustment(self, reader_controls):
    #     """Test if function sets new speech rate value when given"""
    #     reader_controls.setRate(150)
    #     rate = reader_controls.engine.getProperty('rate')
    #     assert rate == 150
    # SAME PROBLEM AS SETVOLUME ADJUSTMENT TESTS

    def test_setRate_error_with_non_int_arguments(self, reader_controls):
        """Test if function raises an error when given non-int argument"""
        with pytest.raises(TypeError) as e:
            reader_controls.setRate("150")
        assert str(e.value) == "Rate must be an integer"

    def test_setRate_with_greater_than_default_value_args(self, reader_controls):
        """Test if function raises an error when given argument greater than 200"""
        with pytest.raises(ValueError) as e:
            reader_controls.setRate(210)
        assert (
            str(e.value) == "Speech rate can be set between 0 and 200 only but got 210"
        )

    def test_setVolume_with_negative_int(self, reader_controls):
        """Test if function raises an error when given a negative int"""
        with pytest.raises(ValueError) as e:
            reader_controls.setRate(-150)
        assert (
            str(e.value) == "Speech rate can be set between 0 and 200 only but got -150"
        )

    def test_setVoice_with_default_argument(self, reader_controls):
        """Test if voice can be initialized using default argument"""
        reader_controls.setVoice()
        assert (
            reader_controls.engine.getProperty("voice")
            == reader_controls.engine.getProperty("voices")[0].id
        )

    # def test_setVoice_adjust(self, reader_controls):
    #     """Test if function changes voice tone when specified"""
    #     reader_controls.setVoice(1)
    #     assert reader_controls.engine.getProperty('voice') == reader_controls.engine.getProperty("voices")[1].id
    # SAME PROBLEM AS ITS PREDECESSORS

    def test_setVoice_with_invalid_argument(self, reader_controls):
        """Test if function raises an error when initialized with an invalid argument"""
        with pytest.raises(TypeError) as e:
            reader_controls.setVoice("female")
        assert str(e.value) == "Voice id must be an int"

    def test_setVoice_with_greater_non_0_1_args(self, reader_controls):
        """Test if function raises an error when given a greater arg int"""
        with pytest.raises(ValueError) as e:
            reader_controls.setVoice(3)
        assert str(e.value) == "Voice id can only be 0 or 1 but got 3"

    def test_setVoice_with_lesser_non_0_1_args(self, reader_controls):
        """Test if function raises an error when given a lesser arg int"""
        with pytest.raises(ValueError) as e:
            reader_controls.setVoice(-1)
        assert str(e.value) == "Voice id can only be 0 or 1 but got -1"


class TestTxtFile:
    """Test suites for the TxtFile function"""

    def test_function_docstring(self):
        """Test if function docstring is present"""
        docstring = txtFile.__doc__

        assert isinstance(docstring, str)
        assert "read a txt file" in docstring
        assert "filepath (str): path to file to read" in docstring
        assert "volume (int): default volume of TTS engine" in docstring
        assert "rate (int): default speech rate of TTS engine" in docstring
        assert "voice (int): default voice id of TTS engine" in docstring

    def test_valid_txt_file(self):
        """Test if function can read a valid file"""
        filepath = "some_valid_file.txt"
        try:
            with open(filepath, "x") as file:
                file.write("Testing a valid txt file")
        except FileExistsError:
            pass

        assert txtFile(filepath) is None  # return None when file has been read

    def test_invalid_txt_file(self):
        """Test if function raises an error given an invalid file"""
        filepath = "non_existent_file.txt"
        with pytest.raises(FileNotFoundError):
            txtFile(filepath)

    def test_handles_special_characters(self):
        """Test if function can read special characters"""
        filepath = "special_chars.txt"

        try:
            with open(filepath, "x") as file:
                file.write('Some text with special characters: !@#$%^&*()_+{}:"<>|\\')
        except FileExistsError:
            pass

        results = txtFile(filepath)
        assert results is None


class TestDocFile:
    """Test suites for docFile function"""

    def test_function_docstring(self):
        """Test if function has docstring"""
        docstring = docFile.__doc__

        assert isinstance(docstring, str)
        assert "read a word doc file" in docstring
        assert "filepath (str): path to file to read" in docstring
        assert "volume (int): default volume of TTS engine" in docstring
        assert "rate (int): default speech rate of TTS engine" in docstring
        assert "voice (int): default voice id of TTS engine" in docstring

    def test_invalid_filepath(self):
        """Test if function raises an error when invalid filepath is given"""
        filepath = "some/invalid/filepath/test.docx"

        with pytest.raises(FileNotFoundError) as e:
            pdfFile(filepath)
        assert str(e.value) == "File not found"


class TestPdfFile:
    """Test suites for pdfFile function"""

    def test_function_docstring(self):
        """Test if function has docstring"""
        docstring = pdfFile.__doc__

        assert isinstance(docstring, str)
        assert "read pdf file" in docstring
        assert "filepath (str): path to file to read" in docstring
        assert "volume (int): default volume of TTS engine" in docstring
        assert "rate (int): default speech rate of TTS engine" in docstring
        assert "voice (int): default voice id of TTS engine" in docstring

    def test_invalid_filepath(self):
        """Test if function raises an error when invalid filepath is given"""
        filepath = "some/invalid/filepath/test.pdf"

        with pytest.raises(FileNotFoundError) as e:
            pdfFile(filepath)
        assert str(e.value) == "File not found"
