#!/usr/bin/env python3
#Project Euler Problem #081: Path sum:two ways
 
f = open("problem_data/p081_matrix.txt", "r")
bla = []
for i in f.read().splitlines():
    bla.append([int(a) for a in i.split(",") if i != ''])


print(bla)

