import sys
import re

def timeConversion(s):
    # Complete this function
    ampm = s[-2] + s[-1]
    print(ampm)
    if ampm == "PM":
        hour, minute, secspm = re.split(":", s)
        if hour != "12":
            hour = int(hour)
            hour += 12
        time = str(hour) + ":" + minute + ":" + secspm
    elif ampm == "AM":
        print("entered am section")
        hour, minute, secspm = re.split(":", s)
        if hour == "12":
            hour = "00"
        time = hour + ":" + minute + ":" + secspm


    return(time[:-2])





s = input().strip()
result = timeConversion(s)
print(result)