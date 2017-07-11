import re

name = input()
testname = re.split(r"[^a-zA-Z]", name)

print(testname)
print(name)
tesname = re.split(r"[^a-zA-Z]+", name)
print(tesname)

tename = re.sub(r'u', 'U', name)
print(tename)