import webbrowser
import os

def search_in_browser(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")

def search_on_computer(file_name):
    for root, dirs, files in os.walk("C:\\"):
        if file_name in files:
            return os.path.join(root, file_name)
    return "Файл не найден."