place = {0: "You are sitting in front of a computer",
         1: "You are on a dark deserted road",
         2: "You are on top of a hill",
         3: "You are in front of a huge glass building",
         4: "You landed up in a valley",
         5: "You are in a dense forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}


loc = 1
while True:
    escape = ", ".join(exits[loc].keys())
    print("Your available exits are: " + escape)
    direction = input("Which direction would you like to go? ").upper()

    if direction == "Q":
        break

    elif direction not in exits[loc].keys():
        print("Cannot enter that realm from here, Try again")
        continue

    else:
        print(place[exits[loc][direction]])
        loc = exits[loc][direction]

else:
    print("Game Over!!!")



