age = 24
print("The age is " + str(age))

print("The age is {0}".format(age))
days = 31
print('There are {0} days in {1}, {2} and {3}'.format(age, "Jan", "Mar", "June"))
print("""Jan {0}
Feb {1}
Mar {0}
Apr {2}""".format(31, 28, 30))


print("My age is %d years" % age)
print("My age is %d %s %d %s" % (age, "years", 6, "months"))


for i in range(1,20):
    print("%2d square is %4d and cube is %2d" % (i, i ** 2, i ** 3))


print("The value of PI is %.12f" % (22 / 7))

for i in range(1,20):
    print("{0:2} square is {1:4} and cube is {2:4}".format(i, i ** 2, i ** 3))


# idented < or >
for i in range(1,20):
    print("{0:2} square is {1:<4} and cube is {2:>4}".format(i, i ** 2, i ** 3))

print("The value of PI is {0:12.4}".format(22 / 7))

