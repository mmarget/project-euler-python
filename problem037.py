#!/usr/bin/env python3
#Project Euler problem #037: Truncatable primes

from helpers import *
count = 0
i = 10
truncs = []
while count < 11:
    check = True
    for j in range(len(str(i))):
        k = int(str(i)[j:])
        if j == 0: l = i
        else: l = int(str(i)[:-j])
        if not isPrime(k) or not isPrime(l): 
            check = False
            break
    if check: 
        truncs.append(i)
        count += 1
        print (i)
    i += 1

print(sum(truncs))

