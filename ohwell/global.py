
a = 1
b = 2

def fun(x, y):
  """global a
  global b"""
  a = x
  b = y
  print ("Within function a = {}, b = {}".format(a, b))

fun(10, 20)
print ("Outside function a = {}, b = {}".format(a, b))
