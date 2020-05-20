import time
from plyer import notification
if __name__ == "__main__":
    notification.notify(
        title="Please Drink Water Now!!",
        message="This time is to drink a glass of water stay hydrated !",
        app_icon="E:\desktop notification\icon2 .ico",
        timeout=3,
    )
    # time.sleep(60*60) it means 60 seconds * 60 minutes = 1 hour means it will remind you every hour without any hesitate after that open the terminal and type pythonw .\main.py it will be running into the ram and will remind every single hour ! because there is a python trick to run the program in background
    time.sleep(60*60)
