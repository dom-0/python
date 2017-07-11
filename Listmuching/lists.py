parrot = ["what", "who", "why", "when's"]
parrot.append("whatever")
for question in parrot:
    print("The parrot is asking " + question)


even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
numbers.sort()
print(numbers)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(sorted(numbers))

list_1 = list()
list_2 = []

if list_1 == list_2:
    print("The lists are equal")