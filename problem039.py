#!/usr/bin/env python3
#Project Euler Problem #039: Integer right triangles
highest = 0
hinum = 0
for p in range(1, 1001):
    print(p)
    count = 0
    for a in range(1, p):
        for b in range(1, p):
            if (a+b) >= p: break
            c = (a**2 + b**2)**0.5
            if a + b + c == p: count += 1
    if count > highest: 
        highest = count
        hinum = p
        print("------",p,highest)

print(count)
