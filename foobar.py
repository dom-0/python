#!/usr/bin/env python

value = input("Please enter the final number : ")

for i in range(value+1):
  value = ""
  if i%3 == 0:
    value = "foo"
    if i%5 == 0:
      value += " bar"
  elif i%5 == 0:
    value = "bar"
  else:
    value = i 
  print (value)
