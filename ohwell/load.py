#!/usr/bin/env python3
import json
import yaml
datastring = ""
with open ("./dict.txt", "r") as fread:
#  datastring = fread.read()
#print (datastring)
#py_obj = json.loads(datastring)
  py_obj = json.load(fread)

print(yaml_obj)


for rec in py_obj:
  print (rec)


print(json.dumps(py_obj))
print(yaml.dump(yaml_obj))
