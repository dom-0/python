
def change():
  a.append(20)
  b = 10
  c = "new string"
  del dict['A']
  print ("\nAfter changing the variables IN the function")
  print ("List = " +  str(a))
  print ("Int = " + str(b))
  print ("String = " + str(c))
  print ("Dict = " + str(dict))

dict = {'A': 'ValueA', 'B': 'ValueB'}
a=[10]
b=1
c="string"
print ("Before calling the function")
print ("List = " +  str(a))
print ("Int = " + str(b))
print ("String = " + str(c))
print ("Dict = " + str(dict))
change()

print ("\nAfter calling the function")
print ("List = " +  str(a))
print ("Int = " + str(b))
print ("String = " + str(c))
print ("Dict = " + str(dict))
