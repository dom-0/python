#!/bin/python3

import sys


n = int(input().strip())
grid = []

grid_i = 0
for grid_i in range(n):
    grid_t = str(input().strip())
    grid.append(grid_t)


for i in range(n):
    row_i= list(map(int, list(grid[i])))
    grid[i] = row_i


for i in range(1, n-1):
    for j in range(1, n-1):
        try:
            if (grid[i][j] > grid[i][j-1]) and (grid[i][j] > grid[i][j+1]) and (grid[i][j] > grid[i+1][j]) and (grid[i][j] > grid[i-1][j]):
                grid[i][j]="X"
        except:
            continue

for i in range(len(grid)):
    for j in range(len(grid)):
        print(grid[i][j], end="")
    print("")