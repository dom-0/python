import time


time_here = time.localtime(time.time())

print("Year is {0}, month is {1}, day is {2}".format(time_here.tm_year, time_here.tm_mon, time_here.tm_mday))
