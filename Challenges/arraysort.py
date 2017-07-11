a = [100, 200, 100, 300, 50, 50]

### count the occurences of each element and display in a descending order
### incase of match display the lowest number first

# store = {}
# newstore = {}
# for i in range(len(a)):
#     try:
#         store[a[i]] += 1
#     except:
#         store[a[i]] = 1
#
#
#
# for i in sorted(store, key=lambda x: store[x]):
#     try:
#         newstore[store[i]].append(i)
#     except:
#         newstore[store[i]] = [i]
#
#
#
# for i in sorted(newstore, reverse=True):
#     for j in sorted(newstore[i]):
#         print(i, j)
skip = []
store = {}
for i in range(len(a)):
    if a[i] in skip:
        continue
    occ = a.count(a[i])
    skip.append(a[i])
    try:
        store[occ].append(a[i])
    except:
        store[occ] = [a[i]]

for i in sorted(store, reverse=True):
    for j in sorted(store[i]):
        print(i, j)

print(store)