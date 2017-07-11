#!/usr/bin/env python

try:
    with open ("./file1.txt") as fh:
	contents = fh.readlines()
        content = fh.read()
except:
    print ("Could not open the file")
else:
    words = content.split()
    print ("File contains " + str(len(words)) + " words")
    print ("Printing read()")
    print (type(content))
    print ("Printing readlines()"), type(contents)
    print (contents)
