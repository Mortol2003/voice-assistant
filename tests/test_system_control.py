import unittest
from system_control import open_application

class TestSystemControl(unittest.TestCase):

    def test_open_application(self):
        # Здесь мы не можем проверить открытие приложения напрямую,
        # но можем убедиться, что os.startfile был вызван с правильными аргументами.
        with unittest.mock.patch('os.startfile') as mock_startfile:
            open_application("блокнот")
            mock_startfile.assert_called_once_with("notepad.exe")

if __name__ == '__main__':
    unittest.main()