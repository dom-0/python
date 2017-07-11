testcases = int(input().strip())

data = []

for x in range(testcases):
    numstones = int(input().strip())

    a = int(input().strip())
    b = int(input().strip())
   # print("a is {} and b is {} and numstones is {}".format(a, b, numstones))
    templist = []
    j = numstones - 1
    for i in range(0, numstones):
        value = (a * i) + (b * (j - i))
        templist.append(value)
    templist.sort()
    data.append(templist)

for i in data:
    for x in sorted(set(i)):
        print(x, end=" ")
    print("")

