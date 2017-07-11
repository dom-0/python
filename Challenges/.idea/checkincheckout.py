entries = int(input())
array = []
people = {}


for i in range(entries):
    checkin, checkout = map(int, input().split())
    temparr = list(range(checkin, checkout))
    array.append(temparr)


for i in range(len(array)):
    for j in range(len(array[i])):
        try:
            people[array[i][j]] += 1
        except:
            people[array[i][j]] = 1
print(people)

array = sorted(people.keys(), key=lambda x: people[x], reverse=True)
print(array)