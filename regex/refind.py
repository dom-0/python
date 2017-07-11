import re

text = "All that glitters is not gold"

iterator = re.finditer(r'\b\w+', text)
for i in iterator:
    print("{} matched from {}".format(i.group(), i.span()))

print("\n\nWe are now going to replace all the gold with diamond")

print(re.sub(r'gold', "silver", text))

value = ord('Z') + 1
print(chr(value))

# for char in range(ord('A'), ord('z') + 1):
#     print(char, chr(char))
#
#
# for i in range(0, 256):
#     print(chr(i))