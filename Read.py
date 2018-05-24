# This is code to record the audio file

import speech_recognition as sr

print("Hello python " , sr.__version__)

r = sr.Recognizer()

harvard = sr.AudioFile('harvard.wav')

with harvard as source:
    audio = r.record(source)
    r.recognize_google(audio)