
import sys
from math import sqrt, ceil, floor
from copy import deepcopy


s = input().strip()
iterstring = iter(s)
length = len(s)
sqroot= sqrt(length)
rowlength = floor(sqroot)
columnlength = ceil(sqroot)
if (rowlength * columnlength) < length:
    rowlength += 1
unenlist = []
enlist=[]
column=0
for i in range(rowlength):
    endcolumn= column + columnlength
    unenlist.append(s[column:endcolumn])
    column = endcolumn

temparray = []
for i in range(columnlength):
    temparray = []
    for j in range(rowlength):
        temparray.append("XX")
    enlist.append(temparray)


for row in range(rowlength):
    for col in range(columnlength):
        try:
            enlist[col][row] = unenlist[row][col]
        except:
            continue
for i in range(columnlength):
    for j in range(rowlength):
        if enlist[i][j] != "XX":
            print(enlist[i][j],end="")
    print(" ", end="")