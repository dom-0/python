Iterations = {}
initial = []
chocolates = [1, 2, 5]
mainlist = []


def createIterations(totaldiff):

    for i in range(0,totaldiff+1):
        if(i == 0):
            Iterations[i] = 0
            continue
        else:
            for x in chocolates:
                count = 0
                if x < i:
                    count = 1 + Iterations[i-x]
                    if not Iterations.get(i):
                        Iterations[i] = count
                    if count < Iterations[i]:
                        Iterations[i] = count
                elif x == i:
                    Iterations[i] = 1
                    break




def recreateinitial(place, diff):

    for i in range(len(initial)):
        if i == place:
            continue
        else:
            initial[i] += diff




occu = int(input())
for i in range(occu):
    entry = int(input())
    entries = list(map(int, input().strip().split()))
    mainlist.append(entries)

for i in mainlist:
    initial = i

    initial.sort(key=int)
    totaldiff = initial[-1] - initial[0]

    createIterations(totaldiff)

## have to find out differences and use the dict Iterations to find out the iterations

    allequal = 0
    count = 0
    while allequal == 0:
        for i in range(1, len(initial)):
            if initial[i-1] < initial[i]:
                diff = initial[i] - initial[i-1]
                count += Iterations[diff]
                recreateinitial(i, diff)
                break
        else:
            allequal = 1

    print(count)









