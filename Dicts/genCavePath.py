place = {"leave": "You are sitting in front of a computer",
         "road": "You are on a dark deserted road",
         "hill": "You are on top of a hill",
         "building": "You are in front of a huge glass building",
         "valley": "You landed up in a valley",
         "forest": "You are in a dense forest"}

exits = {"leave": {"Q": "leave"},
         "road": {"West": "hill", "East": "building", "North": "forest", "South": "valley", "Q": "leave"},
         "hill": {"North": "forest", "Q": "leave"},
         "building": {"West": "road", "Q": "leave"},
         "valley": {"North": "road", "West": "hill", "Q": "leave"},
         "forest": {"West": "hill", "South": "road", "Q": "leave"}}



places = ""
for start in exits:
    if start == "leave":
        continue

    for destination in exits:
        if destination == "leave" or destination == "start":
            continue






loc = "road"
while True:
    print(place[loc])
    print("Where do you want to go? You have the following choices: ", end="")
    for key in place:
        if loc == key:
            continue
        else:
            print(key, end=" ")
    print(":", end=" ")

    dest = input()

    if dest == "leave":
        break
    else:
        loc = dest





