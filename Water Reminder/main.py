import time
from plyer import notification
import re
import asyncio

message = input("what should we remind you of?\n")
input2 = input("time\n")
unit =  re.findall(r'(s|sec|secs|seconds|m|min|mins|h|hr|hrs|hours)', input2)
period = re.findall(r'[0-9]+', input2)
period = float(period[0])
if __name__ == "__main__":
    while True:
        notification.notify(
            title = f"{message}",
            message = f"{message}",
            timeout = 12
        )
        async def reminder():
            seconds = ['s','sec','secs','second','seconds']
            minutes = ['m','min','mins','minute','minutes']
            hours = ['h','hr','hrs','hour','hours'] 
            if (unit in seconds):
                await asyncio.sleep(period)
            elif (unit in minutes):    
                await asyncio.sleep(period*60)
            elif (unit in hours):
                await asyncio.sleep(period*3600)

        asyncio.run (reminder())       
