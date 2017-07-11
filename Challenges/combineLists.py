numbers = int(input().strip())
listofdates = []


for i in range(numbers):
    start, end = map(int, input().strip().split())
    listofdates.append(list(range(start, end+1)))

listofdates.sort()

listofdates = list(map(set, listofdates))
print(listofdates)

for i in range(len(listofdates)-1):

    if listofdates[i] & listofdates[i+1]:
        listofdates[i] = listofdates[i] | listofdates[i+1]
        listofdates[i+1] = {"Ignore This"}

for i in listofdates:
    if "Ignore This" in i:
        continue
    else:
        print("({}, {})".format(min(i), max(i)))