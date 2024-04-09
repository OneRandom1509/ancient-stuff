import getpass
import os

from plyer import notification
from time import sleep


print("Reminder is online!")
while True:
    notification.notify(
        title = "Formula time!!",
        message = "Look up and try to memorise a formula!",
        timeout = 30
    )
    sleep(3600.0)

