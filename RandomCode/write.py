cities = ["New York", "Amsterdam", "Bangalore", "San Jose", "Paris", "Tel Aviv"]

with open("cities.txt", 'w') as file_city:
    for city in sorted(cities):
        print(city, file=file_city)

print("Finished creating cities file")
