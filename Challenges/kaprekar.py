# https://www.hackerrank.com/challenges/kaprekar-numbers?h_r=next-challenge&h_v=zen

from math import floor

start = int(input().strip())
end = int(input().strip())
success = 0
for i in range(start, end+1):
    square = i**2
    square = str(square)
    middle = floor(len(square)/2)
    firsthalf = square[0:middle]
    last = square[middle:]
    firsthalf = "".join(firsthalf)
    last = "".join(last)
    try:
        firsthalf = int(firsthalf)
    except:
        firsthalf = 0
    try:
        last = int(last)
    except:
        last = 0

    if (firsthalf + last) == i:
        print("{}".format(i), end = " ")
        success = 1
    else:
        continue

if success == 0:
    print("INVALID RANGE")