num = int(input("Enter the number: ").strip())
count = 0
for i in range(3, num, 2):

    for x in range(3, (i // 3) + 1):
        if i % x == 0:
            break
    else:
        print(i)
        count += 1
print('-' * 40)
print(count)

