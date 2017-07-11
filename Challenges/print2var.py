a = 12345.9789

print("{0:0>20.2f}".format(a))

b = "{0:0>20.2f}".format(a)
print(b)

import math

c = round(a, 0)
print(c)

c = int(a)
print(c)