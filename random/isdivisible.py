number = int(input("Please enter a positive number less than 1 million : "))

whole_range = range(7, 1000000, 7)

if number in whole_range:
    print("The number {0} is divisible by 7, 7 x {1} = {0}".format(number, whole_range.index(number) + 1))
else:
    print("The number {0} is not divisible by 7".format(number))
