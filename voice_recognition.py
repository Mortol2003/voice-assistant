import vosk
import sys
import os
import sounddevice as sd
import numpy as np
import pyttsx3

def initialize_recognizer(model_path):
    if not os.path.exists(model_path):
        print(f"Модель не найдена: {model_path}")
        sys.exit(1)

    model = vosk.Model(model_path)
    recognizer = vosk.KaldiRecognizer(model, 16000)
    return recognizer

def recognize_speech(recognizer):
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1) as stream:
        print("Listening...")
        while True:
            data = stream.read(4000)
            if not data:
                break
            
            # Преобразуем данные в массив NumPy
            audio_data = np.frombuffer(data[0], dtype=np.int16)

            # Проверяем результат распознавания
            if recognizer.AcceptWaveform(audio_data.tobytes()):
                result = recognizer.Result()
                print(result)  # Выводим результат для отладки
                return result
            else:
                partial_result = recognizer.PartialResult()
                print(partial_result)  # Выводим частичный результат для отладки

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()