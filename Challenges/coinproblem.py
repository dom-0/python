# Given number N, Find the least number of perfect square number sum needed to get N.
#
# Example :
# n=5 (4+1) i.e. 2
# n=7 (4+1+1+1) i.e. 4
# n=12 (4+4+4) i.e 3
# n=20 (16+4) i.e. 2

def findminset(num):

    times={}
    for i in range(0, num+1):
        if i == 0:
            times[i] = 0
            continue
        for square in numbers:
            if i in numbers:
                times[i] = 1
                break
            elif square < i:
                j = i - square
                temp = 1 + times[j]
                if times.get(i):
                    if temp < times[i]:
                        times[i] = temp
                else:
                        times[i] = temp

    return(times[num])


num = int(input("Enter the number: "))
numbers = []
for i in range(1, num // 2):
    i = i**2
    if i <= num:
        numbers.append(i)
numbers.sort()
print(numbers)
minset = findminset(num)
print(minset)
