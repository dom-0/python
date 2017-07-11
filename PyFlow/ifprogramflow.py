name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))

if age >= 18:
    print("You are old enough to vote")
elif age < 18:
    print("Please wait for another {0} years to vote".format(18 - age))