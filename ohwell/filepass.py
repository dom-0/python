#!/usr/bin/env python3

with open("/etc/passwd", "r") as passfile:
  for line in passfile:
    if "root" in line.lower():
      print(line, end="")


with open("/etc/services", "r") as serv:
  lines = serv.readlines()
print(lines)


name = "arnab sen"
print(name[::-2])
