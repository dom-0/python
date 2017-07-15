length, bdigit = list(map(int, input().split()))
numbers  = list(map(int, input().split()))
matched = 0
a = b = c = 0
#tri = []
count = 0
for i in range(0, length):
    for j in range(i+1, length):
        if (numbers[j] - numbers[i]) == bdigit:
            #print("{} {} {} {}===".format(bdigit, numbers[j] - numbers[i], i, j))
            matched += 1
            if matched == 1:
                #a, b = i, j
                i, j = j, j+1
            elif matched == 2:
                #c = j
                #tri.append((numbers[a], numbers[b], numbers[c]))
                count += 1
                matched = 0
                break
                #print("Looped for i={} j={}".format(i, j))
    matched = 0


print(count)