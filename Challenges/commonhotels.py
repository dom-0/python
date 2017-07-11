number = int(input("Users: "))

hotelList = []
for hotels in range(number):
    visited = input().split()
    hotelList.append(visited)
print(hotelList)
for user in range(len(hotelList)):
    print(hotelList[user])
    hotelList[user] = set(hotelList[user])
    print(hotelList[user])



commonset = hotelList[0]
for j in range(1, len(hotelList)):
    if commonset & hotelList[j]:
        commonset = commonset & hotelList[j]
    else:
        commonset = set()
        break

for i in commonset:
    print(i, end=" ")
print("")
