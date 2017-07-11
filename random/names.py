name ={}



def main():
    with open ("./names", 'r') as FH:
        lines = FH.readlines()

    for line in lines:
        line = line.rstrip()
        (lname, fname) = line.split(r',')
        #    print (lname, fname)
        try:
            name[lname].append(fname)
        except:
            name[lname]=[fname]

    for i in sorted(name, key=length, reverse=True):
        print ("%s => %s" %(i, name[i]))


def length(lastname):
    return len(name[lastname])



#  for key in sorted(name, key=len):
#    print ("%s = %s" %(key, name[key]))

#def length(a):
#  return len(name[a])

if __name__ == '__main__':
    main()



##### names
# Senaaa, Arnab
# Senaaa, X
# Senaaa, y
# Sehxxxx, Lei
# Abas, G
# Ater, K
# Termi, O
# Sehxxxx, i
# Sehxxxx, io
# Sehxxxx, ii
# Sehxxxx, illl