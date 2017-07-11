# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm


entries = int(input())
arr = []

def findi(string):
    passed = 0
    for i in range(len(string)-1, 0, -1):
        if string[i-1] < string[i]:

            passed = 1
            return(i)
    if passed == 0:
        return("no answer")


def findj(cmpchar, substring):
    tempstring = sorted(substring)
    for x in tempstring:
        if x > cmpchar:
            return(substring.index(x))

for i in range(entries):
    string = input().strip()
    arr.append(string)

for string in arr:
    string = list(string)

    i=findi(string)
    if i == "no answer":
        print("no answer")
        continue
    pivotstring = string[0:i]
    substring = string[i:]
    cmpchar = string[i-1]

    j=findj(cmpchar, substring)
    j += i

    string[i-1], string[j] = string[j], string[i-1]
    pivotstring = string[0:i]
    substring = sorted(string[i:])

    for n in pivotstring:
        print(n, end="")
    for n in substring:
        print(n, end="")
    print("")