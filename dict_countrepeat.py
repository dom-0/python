names = {'Arnab': 'Sen',
         'Sudeshna': 'Sen',
         'X': 'Abcd',
         'Y': 'XYZ'
        }

count = {}

for value in names.values():
    try:
       count[value] = count[value] + 1
    except:
       count[value] = 1

for name in count:
    print (name + "\t\t" + str(count[name]))
