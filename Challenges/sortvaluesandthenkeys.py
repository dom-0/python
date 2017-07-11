y={100:1, 90:4, 99:3, 92:1, 101:1, 80:3}


### automatically sorts lowest key incase of a tie

# Highest value and in case of a tie - highest key
print("Highest value and in case of a tie - highest key")
for i in sorted(y.items(), key=lambda x: (x[1],x[0]), reverse=True):
    print(i)

# Highest value and in case of a tie - lowest key
print("\nHighest value and in case of a tie - lowest key")

for i in sorted(y.items(), key=lambda x: x[1], reverse=True):
    print(i)

print("\nLowest value and in case of a tie - lowest key")
for i in sorted(y.items(), key=lambda x: x[1]):
    print(i)

print("\nLowest value and in case of a tie - highest key")
for i in sorted(y.items(), key=lambda x: (x[1],-x[0])):
    print(i)