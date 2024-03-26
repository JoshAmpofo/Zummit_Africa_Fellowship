#!/usr/bin/env python3

#### CONTORL FUNCTIONS FOR FILE READER ####

import pyttsx3


class FileReaderControls:
    """creates a class for all controls of the file reader"""

    def __init__(self):
        """initialize reader engine"""
        self.engine = pyttsx3.init()

    def setVolume(self, arg=25):
        """
        volume controls

        Arg(s):
            arg(str -> int): volume set for TTS engine.
                             default value set to 25
        """
        # error checks
        if not isinstance(arg, int):
            raise TypeError("Volume must be an integer")
        if arg < 0 or arg > 100:
            raise ValueError(f"Volume can be set between 0 and 100 only but got {arg}")
        # set controls
        volume = self.engine.getProperty("volume")
        if arg >= 25:
            return self.engine.setProperty("volume", volume+arg)
        elif arg <= 25:
            return self.engine.setProperty("volume", volume-arg)
        

    def setRate(self, arg=20):
        """
        speech rate controls

        Arg(s):
            arg (str -> int): voice spped rate for TTS engine.
                              default value set to 45
        """
        # error checks
        if not isinstance(arg, int):
            raise TypeError("Volume must be an integer")
        if arg < 0 or arg > 100:
            raise ValueError(
                f"Speech rate can be set between 0 and 100 only but got {arg}"
            )
        # set controls
        rates = self.engine.getProperty("rate")
        if arg >= 20:
            return self.engine.setProperty("rate", rates+arg)
        elif arg <= 20:
            return self.engine.setProperty("rate", rates-arg)
        

    def setVoice(self, id=0):
        """
        file reader voice choice

        Arg(s):
            id (str -> int): voice id for TTS engine
                             default id set to 0 (male voice)
        """
        # error checks
        if not isinstance(id, int):
            raise TypeError("Voice id must be an integer")
        if id < 0 or id > 1:
            raise ValueError(f"Voice id can only be 0 or 1 but got {id}")
        # set controls
        voices = self.engine.getProperty("voices")
        if id > 0:
            return self.engine.setProperty("voice", voices[id].id)
        elif id == 0:
            return self.engine.setProperty("voice", voices[id].id)
        
