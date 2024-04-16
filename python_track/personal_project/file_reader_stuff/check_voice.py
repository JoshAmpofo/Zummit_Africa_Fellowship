#!/usr/bin/env python3

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
rates = engine.getProperty('rate')
engine.setProperty('rate', rates-50)
engine.setProperty('voice', voices[1].id)
engine.say('The quick brown fox jumped over the lazy dog')
engine.runAndWait()
    #print(voice.id)
    #print(voice.name)
    #print(voice.age)
    #print(voice.gender)