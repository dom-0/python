#!/usr/bin/env python3


with open ("./table", "w") as ftable:
  for i in range(1,11):
    for j in range(1,13):
      print ("{0:5} times {1:3} is {2:<10}".format(i, j, i*j), file=ftable)
    print ("="*30, file=ftable)
