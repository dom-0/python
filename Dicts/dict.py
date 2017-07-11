fruit = {"orange": "yellow",
         "banana": "green",
         "apple": "red"}

tup = tuple(fruit.items())
print(tup)

new_fruit = dict(tup)
print(new_fruit)