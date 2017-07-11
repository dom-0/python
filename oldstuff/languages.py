favorite_languages = {
       'jen': ['python', 'ruby'],
       'sarah': ['c'],
       'edward': ['ruby', 'go'],
       'phil': ['python', 'haskell'],
       }


for user in  favorite_languages:
    print (user + ":")
    for languages in favorite_languages[user]:
        print ("\t\t" + languages.upper())

