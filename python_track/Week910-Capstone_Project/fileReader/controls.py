#!/usr/bin/env python3

#### CONTORL FUNCTIONS FOR FILE READER ####
import pyttsx3

class FileReaderControls:
    """creates a class for all controls of the file reader"""

    def __init__(self):
        """initialize reader engine"""
        self.engine = pyttsx3.init()

    def setVolume(self, arg=1.0):
        """
        volume controls

        Arg(s):
            arg(str -> float): volume set for TTS engine.
                             default value set to 0.5
        """
        # error checks
        if not isinstance(arg, float):
            raise TypeError("Volume must be a float")
        if arg < 0.0 or arg > 1.0:
            raise ValueError(f"Volume can be set between 0.0 and 1.0 only but got {arg}")
        # set controls
        self.engine.setProperty("volume", arg)
        

    def setRate(self, arg=200):
        """
        speech rate controls

        Arg(s):
            arg (str -> int): voice speed rate for TTS engine.
                              default value set to 200 words per minute
        """
        # error checks
        if not isinstance(arg, int):
            raise TypeError("Rate must be an integer")
        if arg < 0 or arg > 200:
            raise ValueError(
                f"Speech rate can be set between 0 and 200 only but got {arg}"
            )
        # set controls
        self.engine.setProperty("rate", arg)
        

    def setVoice(self, id=0):
        """
        file reader voice choice

        Arg(s):
            id (str -> int): voice id for TTS engine
                             default id set to 0 (male voice)
        """
        # error checks
        if not isinstance(id, int):
            raise TypeError("Voice id must be an int")
        if id != 0 and id != 1:
            raise ValueError(f"Voice id can only be 0 or 1 but got {id}")
        # set controls
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[id].id)