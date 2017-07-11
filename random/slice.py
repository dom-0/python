decimals = range(0,101)

if decimals[3:30:3] == range(3,30,3):
    print("The values of the lists seem to be the same")
else:
    print("The values of the lists seem to differ")

if decimals[3:30:3] is range(3,30,3):
    print("The lists are really one and the same")
else:
    print("No they are not the same list")


a = [1, 2, 4, 5]
b = a

print(a is b)