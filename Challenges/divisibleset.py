a = {'c': 1, 'a': 1, 'b': 2}
print(sum(a.values()))

# for i in a:
#     a[i] = 9
# print(a)

sortednumbers = sorted(a.keys(), key=lambda x: a[x], reverse=True)
print(sortednumbers)

arr = [1, 2, 3, 4]
arr.remove(3)
print(arr)