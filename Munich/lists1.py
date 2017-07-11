list_1 = [2, 4, 6, 8]
list_2 = list_1

print("Before sorting")
print("list_1 = {0}".format(list_1))
print("list_2 = {0}".format(list_2))

list_2.sort(reverse=True)

print("After sorting")
print("list_1 = {0}".format(list_1))
print("list_2 = {0}".format(list_2))

# as you see, the two lists refer to the same memory location
# inorder to copy lists (make them two seperate lists)
# list_1 = list(list_2)
# or
# list_2 = sorted(list_1)

list_3 = [list_1, list_2]
print(list_3)