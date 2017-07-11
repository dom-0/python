#!/bin/python3

import sys
mainlist = []

def findP(match, templist):
    match = str(match)
    templist = str(templist)
    
    arr = []
    x = 0
    while True:

        if match in templist:

            x = x + templist.index(match)
            arr.append(x)
            x += 1
            templist = templist[templist.index(match)+1:]

        else:
            break
    return(arr)


t = int(input().strip())
for a0 in range(t):
    R,C = input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = [] ### contains the main array
    G_i = 0
    for G_i in range(R):
        G_t = str(input().strip())
        G.append(G_t)
    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []  ### contains the sub array
    P_i = 0
    for P_i in range(r):
        P_t = str(input().strip())
        P.append(P_t)

    condition = 0
    for i in range(len(G)):

        if i + r > R:
            if condition == 0:
                mainlist.append("NO")
                break
            else:
                break
        row_G = G[i]
        locations = []
        locations = findP(P[0], row_G)

        for j in locations:

            for x in range(1, len(P)):
                if P[x] != G[i+x][j:j+c]:
                    break
            else:
                mainlist.append("YES")
                condition = 1
                break


print(mainlist)

