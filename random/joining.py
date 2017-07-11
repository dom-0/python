a = [1, 2, 4, 8]
b = [9, 10, 11, 3]


c = a + b
print(c)

x = {'A': 1, 'B': 2}
y = {'C': 3, 'D': 4}
z = x.copy()
z.update(y)
print(z)
print(z.get('E', 12))