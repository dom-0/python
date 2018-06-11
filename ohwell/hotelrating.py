#!/usr/bin/env python3

num = input ("Enter the number of hotels to review: ")
HOTELS = {}
for i in range(int(num)):
  data = input ("Enter the ID and the rating of the hotel: ")
  hid, hrating = data.split()
  hid = int(hid)
  hrating = int(hrating)

  if HOTELS.get(hid):
     HOTELS[hid].append(hrating)
  else:
     HOTELS[hid] = [hrating]

for hotel in HOTELS:
  HOTELS[hotel] = sum(HOTELS[hotel])//len(HOTELS[hotel])


print (HOTELS)
