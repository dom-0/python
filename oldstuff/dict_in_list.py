list = [{"Name": "Arnab", "Surname": "Sen"}, 
        {"Name": "XYZ", "Surname": "Blah"}]

print (list[0]["Surname"])
for rec in list:
  print (rec["Name"] + "\t\t" + rec["Surname"])
