set1 = set(range(10, 34))
set2 = set(range(30, 40))
set3 = set(range(9, 12))

if set2 & set1:
    print(sorted(set1 | set2))

set1.add(1115)
print(sorted(set1))