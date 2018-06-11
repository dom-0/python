#!/usr/bin/env python3

with open ("dict.txt", "r") as fdict:
  dictobj = fdict.readlines()
print (dictobj)
dictobj = list(dictobj)
dictobj = eval(dictobj)

for rec in dictobj:
  print(rec)
