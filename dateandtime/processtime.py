import time

start_time = time.process_time()

num = int(input().strip())

for i in range(num):
    j = i**10

end_time = time.process_time()

print("Time spent processing: {} seconds".format(end_time - start_time))
timex = end_time - start_time

print("epoch time: " + time.strftime("%c", time.localtime(time.time())))
print("epoch time: " + time.strftime("%c", time.gmtime(time.time())))
print(time.tzname)

if time.daylight != 0:
    print("Day light savings is in effect at this moment")
else:
    print("Day light savings is not in effect at this moment")

