import time
import random

input("Press enter to start")
rand = random.randint(0,6)
print(rand)
time.sleep(rand)
start_time = time.perf_counter()
input("Press enter FAST!!!")
end_time = time.perf_counter()


print("Started at: " + time.strftime("%I:%M:%S %p", time.localtime(start_time)))
print("Ended at:   " + time.strftime("%X", time.localtime(end_time)))
print("Today is:   " + time.strftime("%a", time.localtime(time.perf_counter())))

print("Time taken: {0} seconds".format(end_time - start_time))
