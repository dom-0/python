
def rotate(letter, k):
    if ord(letter) in range(ord('A'), ord('Z')+1):
        tempnum = ord(letter) + k - ord('A')
        tempnum = tempnum % 26
        tempnum += ord('A')

    elif ord(letter) in range(ord('a'), ord('z')+1):

        tempnum = ord(letter) + k - ord('a')
        tempnum = tempnum % 26
        tempnum += ord('a')
    else:
        tempnum = ord(letter)


    return(chr(tempnum))



n = int(input().strip())
s = input().strip()
k = int(input().strip())
encrypted = ""
for letter in s:
    encrypted += rotate(letter, k)

print(encrypted)