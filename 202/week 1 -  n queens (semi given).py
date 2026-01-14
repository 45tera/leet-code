# brute force - list + check

#check conflict in diagonals
import itertools

def conflict(i1, j1, i2, j2):
    return (i1-i2 == j1-j2) or (i1 - i2 == - (j1-j2))
  
#check conflict horizontally + vertically?


