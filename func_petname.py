def pet_name(pet="Duck", name="Donald"):
  """Displays information about a pet"""
  print ("I have a pet " + pet + " and his name is " + name)


wpet = raw_input("What pet do you have? ")
wname = raw_input("What is his name? ")

pet_name(name=wname, pet=wpet)
pet_name()
