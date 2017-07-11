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

print("calculating 29.08.2011 11:05:02 + 5 days")

epoch_start = time.mktime(time.strptime(date_time, pattern))
add_to_epoch = 60 * 60 * 24 * 5
epoch_end = epoch_start + add_to_epoch

print(time.strftime("%c", time.localtime(epoch_end)))