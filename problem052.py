#!/usr/bin/env python3
#Project Euler Problem #052: Permuted multiples
i = 1
bla = True
while bla:
    xy = True
    for x in range(2, 7):
        if sorted(list(str(i*x))) != sorted(list(str(i))):
            xy = False
            break
    if i % 10000 == 0: print(i)
    if xy:
        print(i)
        bla = False
    i += 1

