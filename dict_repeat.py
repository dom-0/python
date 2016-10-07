names = {'Arnab': 'Sen',
         'Sudeshna': 'Sen',
         'X': 'Abcd',
         'Y': 'XYZ',
         'Z': 'Abcd'
        }

surnames = {}

for name in names:
    list = []
    list.append(name)

    try:
      #surnames[names[name]].extend(list) # either of them should work
      surnames[names[name]].append(name)
    except:
      surnames[names[name]] = list

for name in surnames:
    print (name + "\t" + str(len(surnames[name])) + "\t\t" + str(surnames[name]))

