first = {"e": "east",
         'w': "west",
         's': "south",
         'n': "north"}

second = {"nw": "north west",
          "se": "south east"}


# third = first
# third.update(second)
# print(third)

third = first.copy()
third.update(second)

print(third)