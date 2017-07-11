#!/usr/bin/env python

pets= []

while input != "quit":
  input = raw_input("Enter the name of the pet: ")
 
  pets.append(input)
print ("\n\n" + str(pets))
remove = raw_input("Which pet would you like to remove? ")

while remove in pets:
  pets.remove(remove)

print (pets)
