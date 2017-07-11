cities = []

with open("cities.txt") as cities_file:
    city = cities_file.readline()
    while city:
        cities.append(city)
        city = cities_file.readline()

for city in sorted(cities, reverse=True):
    print(city, end="")