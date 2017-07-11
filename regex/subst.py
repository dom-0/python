import re

name = input("Enter your name please: ").strip()

pattern = re.compile(r'^(\w+)\W+(\w+)$')

lname, fname = pattern.sub(r'\2 \1', name).split()

print("I reversed your name: {}, {}".format(lname, fname))