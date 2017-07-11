text = "abababacdabad"

match = "aba"
subtext = text
x = 0
while True:

    if match in subtext:
        print("matched at {}".format(x + subtext.index(match)))
        x += 1
        x += subtext.index(match)
        subtext = subtext[subtext.index(match)+1:]
    else:
        break