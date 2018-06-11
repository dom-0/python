#Complete the function below.

hotel ={}
def  best_hotels():
    hotelNumber = int(input())
    for i in range(0, hotelNumber):
        hotelIDhotelScore = input()
        hotelID, hotelScore = hotelIDhotelScore.split()
        hotelID = int(hotelID)
        hotelScore = int(hotelScore)
        if hotelID in hotel:
            hotel[hotelID].append(hotelScore)
        else:
            hotel[hotelID] = [hotelScore]
    for hotelIDs in hotel:
        noRatings = len(hotel[hotelIDs])
        avgScore = sum(hotel[hotelIDs]) / noRatings
        hotel[hotelIDs] = avgScore

    for ranking in sorted(hotel.items(), key=lambda x: x[1], reverse=True):
        print(ranking[0])


best_hotels()
