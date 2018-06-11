#!/usr/bin/env python

d = {"a": 2, "b": 4, "c": 1}

for i in sorted(d.keys()):
  print ("{}\t{}".format(i, d[i]))

for dic in sorted(d.items(), key=lambda x: x[1]):
  print(dic)

