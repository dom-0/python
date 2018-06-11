#!/usr/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    h, m, sec = s.split(':')
    if (sec[-2] == "p") or (sec[-2] == "P"):
        h = int(h)
        if (h >= 1 and h <= 11):
            h = h + 12
        h = str(h)
    elif (sec[-2] == "a") or (sec[-2] == "A"):
        h = int(h)
        if (h == 12):
            h = "00"
    return(h + ":" + m + ":" + sec[:-2])
        
     

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result)
