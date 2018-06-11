#!/usr/bin/env python3

import re

line = input ("Enter the phone number :")
line = line.rstrip()

repObj = re.sub(r'\D', "", line)
print (repObj)


