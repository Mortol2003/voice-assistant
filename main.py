from voice_recognition import initialize_recognizer, recognize_speech, speak
from system_control import open_application, close_application, control_wifi, shutdown_system, restart_system
from information_search import search_in_browser, search_on_computer
from media_control import play_music, control_volume
from task_management import add_reminder, check_reminders

def main():
    model_path = "C:\\student\\project\\voice-assistant\\vosk-model-small-ru-0.22"  

    while True:
        command = recognize_speech(recognizer)

        if command:
            command = command.lower()
            
            if "открыть" in command:
                app_name = command.replace("открыть ", "")
                open_application(app_name)
                speak(f"Открываю {app_name}.")
                
            elif "закрыть" in command:
                window_title = command.replace("закрыть ", "")
                close_application(window_title)
                speak(f"Закрываю {window_title}.")
                
            elif "включить Wi-Fi" in command:
                control_wifi(True)
                speak("Wi-Fi включен.")
                
            elif "выключить Wi-Fi" in command:
                control_wifi(False)
                speak("Wi-Fi выключен.")
                
            elif "выключить компьютер" in command:
                shutdown_system()
                
            elif "перезагрузить компьютер" in command:
                restart_system()
                
            elif "поиск" in command:
                query = command.replace("поиск ", "")
                search_in_browser(query)
                
            elif "найти файл" in command:
                file_name = command.replace("найти файл ", "")
                result = search_on_computer(file_name)
                speak(result)
                
            elif "играть музыку" in command:
                file_path = command.replace("играть музыку ", "")
                play_music(file_path)
                
            elif "увеличить громкость" in command:
                control_volume("increase")
                
            elif "уменьшить громкость" in command:
                control_volume("decrease")
                
            elif "напоминание" in command:
                parts = command.split()
                reminder_text = ' '.join(parts[1:-1])
                delay_minutes = int(parts[-1])
                add_reminder(reminder_text, delay_minutes)
                speak(f"Напоминание добавлено на {delay_minutes} минут.")
                
            check_reminders()

if __name__ == "__main__":
    main()