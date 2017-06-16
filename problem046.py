#!/usr/bin/env python3
#Project Euler problem #046: Goldbach's other conjecture
#Find the smallest odd composite that cannot be written as the sum of a prime and twice a square

from helpers import isPrime
limit = 200
compnums = sorted(list(set([i*j for i in range(2, limit) for j in range(2, limit) if i*j % 2 != 0])))
print(len(compnums))

primes = [i for i in range(1, max(compnums)-2) if isPrime(i)]
print(len(primes))
arr = []
sumnums = sorted(list(set([2*(i**2) for i in range(1, int(max(compnums)**0.5))])))
print(len(sumnums))
print("numbers done.")
for cnum in compnums:
    bla = False
    for prime in primes:
        if bla == True: break
        for snum in sumnums:
            if cnum == prime + snum: 
                bla = True
                break
    if bla == False:
        arr.append(cnum)
        print(cnum)

print(min(arr))
