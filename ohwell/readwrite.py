#!/usr/bin/env python3

with open ("/etc/services", "r") as fservice:
  service_file = fservice.readlines()

with open ("./services", "w") as flocal:
  for line in service_file:
    print (line, file=flocal, end='')
