fav_lang = {'Arnab': "C", 'Kerim': 'Java'}
workers = ['Arnab', 'Kerim', 'Gordan']

for user in workers:
    if user in fav_lang.keys():
        print ("\"" + user + ", looks like you have a favorite language and that is " + fav_lang[user])
    else:
        print ("\"" + user + ", looks like you do not have a fav language")

