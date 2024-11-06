import subprocess

def play_music(file_path):
    subprocess.Popen(["start", "", file_path], shell=True)

def control_volume(action):
    if action == "increase":
        subprocess.call(["nircmd.exe", "changesysvolume", "2000"])  
    elif action == "decrease":
        subprocess.call(["nircmd.exe", "changesysvolume", "-2000"])  