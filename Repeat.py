data = {}

print ("Enter your details...")
print ("To quit, type quit !!!")

while True:
    fname = raw_input("Enter your first name: ")
    lname = raw_input("Enter your last name: ")

    data[fname] = lname
    cont = raw_input("Do you want to enter another set of record? [Yes\\Quit] (Default is Yes) :")
    
    if cont.lower() == "quit":
        break

surdata = {}

for key in data:
    try: 
        surdata[data[key]].append(key)
    except:
        surdata[data[key]] = [key]


print (surdata)
