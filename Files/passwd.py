with open("/etc/passwd", 'r') as passwd:
    string = passwd.read()

print(string[0:2])

print('-=' * 40)
with open("/etc/passwd", 'r') as passwd:
    string = passwd.readlines()
print(string[0:2])

print('-=' * 40)
with open("/etc/passwd", 'r') as passwd:
    string = passwd.readline()
print(string[0:2], flush=True)


# list=fh.read() - reads the whole file in a single string char by char
# list = fh.readlines() - reads the whole file as a list of strings line by line
# list=fh.readline() - reads the file line by line. You have to repeat the statement till the end of the file
