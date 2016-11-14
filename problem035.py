#!/usr/bin/env python3
#Project Euler Problem #035: circular primes
#How many circular primes are there below one million?

from helpers import *
count = 0
for i in range(2, 1000001):
    ulu = False
    if isPrime(i) == True:
        ulu = True
        olo = intToArr(i)
        for _ in range(len(str(i))-1):
            olo = rotate(olo)
            if isPrime(arrToInt(olo)) == False: ulu = False
    if ulu == True:
        count += 1
print("There are",count,"circular primes below one million")
