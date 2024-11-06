import unittest
from voice_recognition import initialize_recognizer

class TestVoiceRecognition(unittest.TestCase):

    def test_initialize_recognizer(self):
        model_path = "C:\\student\\project\\voice-assistant\\vosk-model-small-ru-0.22"
        recognizer = initialize_recognizer(model_path)
        self.assertIsNotNone(recognizer)

if __name__ == '__main__':
    unittest.main()