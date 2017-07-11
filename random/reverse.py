string = "Python is a powerful language!!!"

for char in string[::-1]:
    print(char, end="")
print("")

print('*' * 40)

for index in range(len(string)-1, -1, -1):
    print(string[index], end="")
