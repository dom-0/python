
names = ["Luis", "Hector", "Selena", "Emmanuel", "Amish"]
cyclicnames = {}
startwith = ""
depth = 1
for i in range(len(names)):
    for j in range(len(names)):
        if i == j:
            continue

        if names[i][-1].lower() == names[j][0].lower():
            cyclicnames[names[i]] = names[j]
            break


print(cyclicnames)

for name in cyclicnames:
    count = 1
    tempname = name

    while True:

        if cyclicnames.get(cyclicnames[name]):
            count += 1
            name = cyclicnames[name]
        else:
            if count > depth:
                depth = count
                startwith = tempname
                print("Starts with {1} with a count of {0}".format(count, tempname))
                break
            else:
                break


while True:
    if cyclicnames.get(startwith):
        print(startwith)
        startwith = cyclicnames[startwith]
        continue
    else:
        break