import schedule
import time
import datetime

def send_reminder():
    current_time = datetime.datetime.now()
    print(f"Check your email time: {current_time}")
    with open("reminders.txt", "a") as file:
        file.write(f"Check your email time: {current_time}\n")

schedule.every(20).seconds.do(send_reminder)

while True:
    schedule.run_pending()
    time.sleep(1)
