mainlist = []
hashi={}
def sortfunc(var):
    return(var[0])


number = int(input())
for i in range(0, number):
    temparr = []
    tempVar = input()
    a,b = tempVar.split()
    temparr.append(int(a))
    temparr.append(int(b))
    temTuple = tuple(temparr)
    mainlist.append(temTuple)

newlist=sorted(mainlist, key=sortfunc)

for i in range(0, number-1):
    for j in range(i+1, number):
        if(newlist[i][1] > newlist[j][0]):
            # newlist[i]=(newlist[i][0], newlist[j][1])
            newlist[j]=(newlist[i][0], newlist[j][1])
            hashi[newlist[j]]=1

        else:
            continue

print(hashi)