#
# Given a stream of characters (e.g. acacabcatghhellomvnsdb) and a list of words (e.g. ["aca","cat","hello","world"] )
# find and display count of each and every word once the stream ends.(Like : "aca" : 2 , "cat" : 1 , "hello" : 1 , "world" : 0 ).

import re

text = "acacacabcatghhellomvnsdb"

listwords = ["aca","cat","hello","world"]

# for word in listwords:
#     occurences = re.findall(word, text)
#     print("{} occured in {}, {} times".format(word, text, len(occurences)))

for word in listwords:
    count = 0
    temptext = text
    while True:
        if word in temptext:
            count += 1
            index = temptext.index(word)
            temptext = temptext[index+1:]
        else:
            break
    print("{} occured {} times".format(word, count))