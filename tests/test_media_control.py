import unittest
from media_control import control_volume
import subprocess

class TestMediaControl(unittest.TestCase):

    def test_increase_volume(self):
        # Здесь мы не можем проверить изменение громкости напрямую,
        # но можем убедиться, что subprocess.call был вызван с правильными аргументами.
        with unittest.mock.patch('subprocess.call') as mock_call:
            control_volume("increase")
            mock_call.assert_called_once_with(["C:\\Tools\\nircmd\\nircmd.exe", "changesysvolume", "2000"])

    def test_decrease_volume(self):
        with unittest.mock.patch('subprocess.call') as mock_call:
            control_volume("decrease")
            mock_call.assert_called_once_with(["C:\\Tools\\nircmd\\nircmd.exe", "changesysvolume", "-2000"])

if __name__ == '__main__':
    unittest.main()