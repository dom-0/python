number = input().strip()

number = list(map(int, number))

arr = []
for i in range(1, len(number)):
    span = i
    for j in range(0, len(number)):
        if i+j > len(number):
            break
        else:

            arr.append(number[j:i+j])

suma = 0
for alist in arr:
    alist = list(map(str, alist))
    temp = "".join(alist)
    print("Number = {}".format(temp))
    temp = int(temp)
    suma += temp

print("Total sum: {}".format(suma))