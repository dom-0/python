import time

year = input("Enter the year: ").strip()
days = input("Enter the days to advance: ").strip()
days = int(days)
year = int(year) - 1
year = str(year)
date_time = '31.12.' + year + " 00:00:00"
pattern = '%d.%m.%Y %H:%M:%S'
epoch_start = time.mktime(time.strptime(date_time, pattern))

advance = days * 24 * 60 * 60
epoch_end = epoch_start + advance

print(time.strftime("%c", time.localtime(epoch_end)))
