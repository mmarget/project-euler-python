#!/usr/bin/env python3
#Project Euler Problem #049: Prime permutations

from helpers import isPrime
bla = []
for i in  range(1000, 10000):
    print(i)
    for j in range(1, 10000 - 2*i):
        if isPrime(i) and isPrime(i + j) and isPrime(i + 2*j):
            if sorted(list(str(i))) == sorted(list(str(i+j))) and sorted(list(str(i))) == sorted(list(str(i + 2*j))):
                bla.append([i, i+j, i+2*j])

print(bla)
