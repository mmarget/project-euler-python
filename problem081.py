#!/usr/bin/env python3
#Project Euler Problem #081: Path sum:two ways
 
f = open("problem_data/p081_matrix.txt", "r")
matrix = []
for i in f.read().splitlines():
    matrix.append([int(a) for a in i.split(",") if i != ''])
n = len(matrix)
for i in range(2*n-1):
    j = n - 1 - i
    k = n - 1
    while k >= 0 and j < n:
        if j < 0: pass
        else:
            if j == n - 1 and k == n - 1: pass
            elif j == n-1:
                matrix[k][j] += matrix[k+1][j]

            elif k == n-1:
                matrix[k][j] += matrix[k][j+1]
            else:
                matrix[k][j] += min([matrix[k+1][j], matrix[k][j+1]])

                
        j += 1
        k -= 1
    
print(matrix[0][0])

