################################# READ READ
#### This script wont run here in Mac
#### But it works fine
###########################################


import subprocess


p = subprocess.Popen('ls -l', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
(stout, sterr)  = p.communicate()
if (p.returncode != 0):
    print ("Error " + sterr)
else:
    print ("alksjdfklajsdklfjaksdjfkjsd")
    print(stout)