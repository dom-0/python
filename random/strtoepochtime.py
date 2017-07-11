import time

date_time = '29.08.2011 11:05:02'
pattern = '%d.%m.%Y %H:%M:%S'
epoch_start = time.mktime(time.strptime(date_time, pattern))
print("===" + time.strftime("%c", time.localtime(epoch_start)))

date_time = '29.08.2011 12:05:02'
epoch_end = time.mktime(time.strptime(date_time, pattern))

print(epoch_end - epoch_start)

print(time.localtime())
print(time.strptime(date_time, pattern))