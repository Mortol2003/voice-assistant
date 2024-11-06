import os
import subprocess

def open_application(app_name):
    if app_name == "блокнот":
        os.startfile("notepad.exe")
    elif app_name == "калькулятор":
        os.startfile("calc.exe")
    elif app_name == "firefox":
        os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    else:
        print("Приложение не найдено.")

def close_application(window_title):
    subprocess.call(["taskkill", "/F", "/IM", window_title])

def control_wifi(enable):
    if enable:
        os.system("netsh interface set interface 'Wi-Fi' enabled")
    else:
        os.system("netsh interface set interface 'Wi-Fi' disabled")

def shutdown_system():
    os.system("shutdown /s /t 1")

def restart_system():
    os.system("shutdown /r /t 1")