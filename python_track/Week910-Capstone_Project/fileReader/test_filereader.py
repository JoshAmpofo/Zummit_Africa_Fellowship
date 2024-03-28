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
        assert 'creates a class for all controls of the file reader' in docstring
    
    def test_setVolume_docstring(self, reader_controls):
        """Test for the presence of a doctring in setVolume function"""
        docstring = reader_controls.setVolume.__doc__
        assert isinstance(docstring, str)
        assert 'volume control' in docstring
        assert 'arg(str -> float): volume set for TTS engine.' in docstring
        assert 'default value set to 0.5' in docstring
    
    def test_setRate_docstring(self, reader_controls):
        """Test for the presence of a docstring in setRate function"""
        docstring = reader_controls.setRate.__doc__
        assert isinstance(docstring, str)
        assert 'speech rate controls' in docstring
        assert 'arg (str -> int): voice speed rate for TTS engine.' in docstring
        assert 'default value set to 200 words per minute' in docstring
        
    def test_setVoice_docstring(self, reader_controls):
        """Test for the presence of a docstring in setVoice function"""
        docstring = reader_controls.setVoice.__doc__
        assert isinstance(docstring, str)
        assert 'file reader voice choice' in docstring
        assert 'id (str -> int): voice id for TTS engine' in docstring
        assert 'default id set to 0 (male voice)' in docstring
        
    def test_init(self, reader_controls):
        """Test if initialization works without errors"""
        assert isinstance(reader_controls, FileReaderControls)
    
    # TEST MAIN CONTROL FUNCTIONS
    def test_setVolume(self, reader_controls):
       """Test if volume can be initialized with default argument"""
       reader_controls.setVolume()
       volume = reader_controls.engine.getProperty('volume')
       assert volume == 1.0
    
    def test_setRate(self, reader_controls):
        """Test if rate can be initialized with default argument"""
        reader_controls.setRate()
        rate = reader_controls.engine.getProperty('rate')
        assert rate == 200
        
    # def test_setVoice(self, reader_controls):
    #     """Test if voice can be initialized using default argument"""
    #     reader_controls.setVoice(0)
    #     voice_id = reader_controls.engine.getProperty('voices')
    #     assert voice_id == 0
        

