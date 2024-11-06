import vosk
import sys
import os
import wave

def initialize_recognizer(model_path):
    if not os.path.exists(model_path):
        print(f"Модель не найдена: {model_path}")
        sys.exit(1)

    model = vosk.Model(model_path)
    recognizer = vosk.KaldiRecognizer(model, 16000)
    return recognizer

def recognize_speech(recognizer):
    import sounddevice as sd
    import numpy as np

    def callback(indata, frames, time, status):
        if status:
            print(status)
        if recognizer.AcceptWaveform(indata):
            print(recognizer.Result())
        else:
            print(recognizer.PartialResult())

    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1) as stream:
        print("Listening...")
        while True:
            data = stream.read(4000)
            if not data:
                break

def speak(text):
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()