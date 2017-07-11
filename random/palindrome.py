pal_check = input("Please enter a string: ")
# for i in range(0, int(len(pal_check) / 2)):
#     if pal_check[i] != pal_check[-i-1]:
#         print("Not a palindrome")
#         exit(0)
#
# print("Yes it is a palindrome")

if pal_check[::] == pal_check[::-1]:
    print ("Palindrome")
else:
    print ("Not a palindrome!")

for i in range(len(pal_check)-1, -1, -1):
    print(pal_check[i])