import itertools


def matchlist(i, divno):
    # find out if addition of any two integers of the set is not divisible by divno
    for x in range(0, len(i)):
        for y in range(x+1, len(i)):
            if (i[x] + i[y]) % divno == 0:
                return(False)
    else:
        return(True)



length, divno = list(map(int, input().split()))

numbers = list(map(int, input().split()))
span = 0
listofsets = []

b = 0
for i in range(length, 0, -1):
    for x in itertools.combinations(numbers, i):
        if matchlist(x, divno):
            print(len(x))
            b = 1
            break

    if b == 1:
        break


# listofsets.sort(key=lambda x: len(x), reverse=True)
# print(listofsets)

#for i in listofsets:
#    if matchlist(i, divno):
#        print(i)

