import shelve

with shelve.open("shelvefile") as SF:
    SF["apple"] = "lovely fruit"
    SF["banana"] = "is that even a fruit"
    SF["orange"] = "great fruit"

    print(SF["orange"])
print(SF)