arr = [1, 2, 3, 4]

my_iter = iter(arr)
for i in range(0, len(arr)):
    print(next(my_iter))