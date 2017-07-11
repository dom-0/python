number = input()

hotelRatings ={}
newRating={}
for i in range(int(number)):
    hotelID, rating = input().split()
    hotelID = int(hotelID)
    rating = int(rating)
    try:
        hotelRatings[hotelID].append(rating)
    except:
        hotelRatings[hotelID]=[rating]


for i in hotelRatings:
    hotelRatings[i] = sum(hotelRatings[i]) / len(hotelRatings[i])
    try:
        newRating[hotelRatings[i]].append(i)
    except:
        newRating[hotelRatings[i]] = [i]


for i in sorted(newRating, reverse=True):
    for x in sorted(newRating[i]):
        print(x, i)
