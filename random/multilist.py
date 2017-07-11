from copy import deepcopy

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

b = deepcopy(a)

# Solution 1
# for i in range(len(a)):
#     b.append(a[i][:])

# Solution 2
# b = [a[x][:] for x in range(len(a))]


print(a is b)

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end= " ")
        b[j][i] = a[i][j]
    print()

print("*"*40)
print(a is b)
for i in range(len(b)):
    for j in range(len(a[i])):
        print(b[i][j], end=" ")
    print()
