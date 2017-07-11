# IP address section counting
# Count how many sections and the length of each section
# Eg: 1.23232.21.232 should give 4 sections with lengths 1 5 2 3

ip = input("Enter the IP address: ")

secLengths = [0]
for i in ip:
    if i not in ".":
        secLengths[-1] += 1
    else:
        secLengths.append(0)
        continue


print("""Number of Sections: {0}
Length of the Sections: {1}""".format(len(secLengths), secLengths))





