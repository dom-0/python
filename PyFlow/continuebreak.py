items = ["rice", "pasta", "noodles", "ice cream", "oats", "eggs"]

for i in items:
    if i == "ice cream":
        continue  # This would ignore the particular item
    print("{}".format(i), end=' ')

print()
for i in items:
    if i == "ice cream":
        break  # This would stop the loop here
    print("{}".format(i), end=' ')

num = 1
var = 10
num += var

print(num)