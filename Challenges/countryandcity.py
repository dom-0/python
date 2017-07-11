country = {"IN": "India", "US": "USA", "NL": "Nederlands", "IT": "Italy"}
city = {"IN": "Mumbai", "US": "Washington", "IT": "Naples"}

for coun in country:
    if not city.get(coun):
        print("{} has no city".format(coun))

