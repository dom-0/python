
temp = 0
initial = 0
second = 1

listofnumbers= []
listofnumbers.append(initial)
listofnumbers.append(second)
for i in range(0, 28):
    temp = initial + second
    initial, second = second, temp
    listofnumbers.append(temp)

print(listofnumbers)