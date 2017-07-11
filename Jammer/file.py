F = open("workfile",'w')
print(F)
F.write("Hello! This is me you are looking for")
F.close()

F = open("workfile", 'r')
print(F)