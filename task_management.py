from datetime import datetime, timedelta

reminders = []

def add_reminder(reminder_text, delay_minutes):
    reminder_time = datetime.now() + timedelta(minutes=delay_minutes)
    reminders.append((reminder_time, reminder_text))

def check_reminders():
    now = datetime.now()
    for reminder in reminders:
        if reminder[0] <= now:
            print(f"Напоминание: {reminder[1]}")
            reminders.remove(reminder)