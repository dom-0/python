# def compress(string):
#     prev = None
#     cons = 1
#     compressed = ''
#     for i in string:
#         if prev:
#             if prev == i:
#                 cons += 1
#             else:
#                 compressed += prev+str(cons)
#                 cons = 1
#         prev = i
#     compressed += prev+str(cons)
#
#     return compressed


def compress(string):
    compstring=""

    for i in range(len(string)):
        if i == 0:
            count = 1
        else:
            if (string[i] == string[i-1]):
                count += 1
            else:
                compstring = compstring + string[i-1] + str(count)
                count = 1

    compstring = compstring + string[i] + str(count)
    return(compstring)


string = input().strip()
print(compress(string))