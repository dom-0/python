name = input("Enter your name: ")
age = int(input("Enter your age, {0} ".format(name)))

if 18 < age < 31:
    print("Welcome {0}, you are in".format(name))
elif age <= 18:
    print("Please come back after {0} year(s), {1}".format(19 - age, name))
else:
    print("Sorry {0}, but you should have tried {1} years earlier".format(name, age - 30))