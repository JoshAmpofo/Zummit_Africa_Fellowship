import pyttsx3
import sys

#volume_2 = float(sys.argv[1])
engine = pyttsx3.init()

volume = engine.getProperty('volume')
engine.setProperty('volume', volume+0.75)
#print(volume)
engine.say("The quick brown fox")
engine.runAndWait()
