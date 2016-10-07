#!/usr/bin/env python

def sand(name, toppings=["cheese", "potatoe"]):
    print (name + " wants the sandwich to have:")
    while toppings:
       top = toppings.pop()
       print ("\t- " + top)
 
list_Nic = ["Grated cheese", "Mayo", "sausage"]
sand("Nic", list_Nic)
sand(name="X")
