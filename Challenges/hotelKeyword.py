## This is the text editor interface.
## Anything you type or change here will be seen by the other person in real time.


#### input
## hotel search word
## number of hotels
## hotelID
## words space seperated

hotel = {}

searchword = input().strip()
number = int(input().strip())

for i in range(number):
    hotelID = int(input().strip())
    words = input().strip().split()
    for word in words:
        try:
            hotel[word].append(hotelID)
        except:
            hotel[word] = [hotelID]

## hotel = {"great": [121, 132, 121], "nice": [10, 121]}
hotels = []
hotels = hotel[searchword]
templist = []
## hotels = [121, 132, 121]
newdict = {}
for hotel in hotels:
    if hotel in templist:
        continue
    else:
        num = hotels.count(hotel)
        templist.append(hotel)
        try:
            newdict[num].append(hotel)
        except:
            newdict[num] = [hotel]


for occur in sorted(newdict.keys(), reverse=True):
    for i in sorted(newdict[occur]):
        print(i, end=" ")
    print("")