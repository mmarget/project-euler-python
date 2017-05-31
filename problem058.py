#!/usr/bin/env python3
#Project Euler Problem 58: Spiral Primes
from helpers import isPrime
counter = 1
corners = [1]
primes = []
for i in range(2, 1000000):
    length = 2*i -1
    counter += 1
    counter += length - 2
    corners.append(counter)
    if isPrime(counter): 
        primes.append(counter)
    for j in range (3):
        counter += length - 1
        corners.append(counter)
        if isPrime(counter): 
            primes.append(counter)
    perc = len(primes) / len(corners)
    print(perc)
    if perc < 0.1:
        print(corners)
        print(length)
        break
    #print(corners)
#print(corners)
#print(primes)
