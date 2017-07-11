availableExits = ["west", "east", "north east"]

i = ""
while i not in availableExits:
    i = input("Enter the direction: ")
    if i == "quit" or i == "QUIT" or i == "Quit":
        print("Game Over!!!")
        break

else:
    print("Arn't you glad you got out of there? ")