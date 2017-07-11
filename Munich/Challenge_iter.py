animals = ["baboon", "cow", "human", "dog", "elephant"]

itered_animal = iter(sorted(animals))
print(next(itered_animal))

print()
for i in range(len(animals)-1):
    print(next(itered_animal))


