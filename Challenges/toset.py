a = [(1, 2), (3, 4)]

b = set(a)
print(b)

a = [[1, 2], [3, 4]]
print("")
print(a)
for i in range(len(a)):
    a[i] = set(a[i])
print (a)

a = ["asdf", "cd"]
for i in range(len(a)):
    a[i] = set(a[i])
print(a)