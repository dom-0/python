number ="1,32,53232,9929,82382,882"
cleanedNumber = ''
for i in number:
    if i in "0123456789":
        cleanedNumber = cleanedNumber + i

print ("{}".format(cleanedNumber))

for i in range(1, 13):
    for j in range(1, 13):
        print("{0:2} times {1:2} is {2:>5}".format(i, j, i*j), end="\t")
    print()