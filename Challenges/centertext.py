def center_text(*args, sep = ' ', end = "\n", flush=False, file=None):
    string = ""
    for argument in args:
        string = string + str(argument) + sep
    space = 80 - (len(string) // 2)
    string=string.rstrip(sep)
    print(":" * space , end="")
    print(string, end="")
    print(":" * space, end="")

# name = input("Enter a text: ")
center_text("arnab Sen", "xxx", "yyy", sep=":")
