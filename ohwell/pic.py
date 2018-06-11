#!/usr/bin/env python3

import pickle


file_Name = "dict.txt"
# open the file for writing
fileObject = open(file_Name,'r')  
# load the object from the file into var b
b = fileObject.read()
fileObject.close()
print(b)


with open ("./dict1.txt", "wb") as fwrite:
  pickle.dump(b,fwrite)


with open ("./dict1.txt", "rb") as fread:
  x = pickle.load(fread)
x = dict(x)

print(x["Arnab"])
