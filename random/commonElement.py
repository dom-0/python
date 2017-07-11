a = [4, 5, 2, 1, 12, 10, 11, 31]
b = [90, 41, 12, 13, 66, 10, 21, 31, 12]
c = [41, 42, 31, 10 , 12, 11, 43]


set1 = set(a)
set2 = set(b)
set3 = set(c)

commonFirstSec = set(a).intersection(set(b))
commonSecThird = commonFirstSec.intersection(set(c))

print(commonFirstSec)