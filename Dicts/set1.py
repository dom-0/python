farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("=" * 40)

wild_animals = set(["lion", "tiger"])
print(wild_animals)

for animal in wild_animals:
    print(animal)


farm_animals.add("horse")
wild_animals.add("horse")

print(farm_animals)

for animal in farm_animals:
    print(animal)

print("=" * 40)


print(wild_animals)

for animal in wild_animals:
    print(animal)
