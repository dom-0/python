from collections import OrderedDict

a = [1, 2, 3, 1, 9, 7, 2, 1, 10]


b = []
for char in a:
    if char not in b:
        b.append(char)
    else:
        continue

print(b)

print(list(OrderedDict.fromkeys(a)))

print(list(OrderedDict.fromkeys(a)))