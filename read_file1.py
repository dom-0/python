#!/usr/bin/env python

with open ("./file1.txt") as fhandle:
    for line in fhandle:
        print (line.rstrip())
	newline=line.replace('Python','C')
	print (newline)
