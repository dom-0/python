openingbraces = ["(", "{", "["]
oppo = {"{": "}", "[": "]", "(": ")"}
listOpen = []
string = input().strip()

for i in string:
    if i in openingbraces:
        listOpen.append(i)
        print(i + " appended")
    else:
        if i != oppo[listOpen[-1]]:

            print("Not the right syntax")
            exit(0)
        else:
            listOpen.pop()

if len(listOpen) > 0:
    print("Not proper")
else:
    print("perfect!!!")
