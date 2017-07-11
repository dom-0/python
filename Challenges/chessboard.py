length, number = list(map(int, input().split()))
listnumbers = []

listnumbers = list(map(int, input().split()))
listnumbers.sort()
occurences = {}
for i in range(length):
    occurences[listnumbers[i]]=0
while True:
    for i in range(length-1):
        for j in range(i+1, length):
            if (listnumbers[i] + listnumbers[j]) % number == 0:
                occurences[listnumbers[i]]+=1
                occurences[listnumbers[j]]+=1
                print("{} {}".format(listnumbers[i], listnumbers[j]))

    print(occurences)
    sortednumbers = sorted(occurences.keys(), key=lambda x: occurences[x], reverse=True)
    if occurences[sortednumbers[0]] != 0:
        del(occurences[sortednumbers[0]])

    listnumbers.remove(sortednumbers[0])
    length -= 1


    if sum(occurences.values()) == 0:
        break
    for i in occurences:
        occurences[i]=0

print(len(occurences))