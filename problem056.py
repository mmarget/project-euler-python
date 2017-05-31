#!/usr/bin/env python3
#Project Euler Problem #056: Powerful digit sum
hinum = 0

for a in range(1, 101):
    for b in range(1, 101):
        bla = sum([int(i) for i in list(str(a**b))])
        if bla > hinum:
            hinum = bla
            print(hinum)


