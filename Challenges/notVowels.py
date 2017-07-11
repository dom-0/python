vowels = "aeiou"
string = input("Enter the line of text: ")

for char in string:
    if char not in vowels:
        print(char, end="")