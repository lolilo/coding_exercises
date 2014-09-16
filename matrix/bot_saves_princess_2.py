#!/bin/python

# https://www.hackerrank.com/challenges/saveprincess2
def nextMove(n,r,c,grid):
    # find where the princess is
    princess_location = []
    princess_found = False
    
    row = 0
    for row in grid:
        column = 0
        for cell in row: 
            if cell == 'p':
                princess_location.extend(row, column)
                princess_found = True
            column += 1
                
    # check if you are on the same row as the princess, 
    return ""

n = raw_input()
r_c = raw_input().split() # list of r and c
r, c = r_c[0], r_c[1]
#r,c = [int(i) for i in raw_input().strip().split()]
grid = []
# create and array of arrays for the matrix
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,r,c,grid)
