#!/usr/bin/env python3
#Project euler Problem 50: consecutive prime sum

from helpers import isPrime

bla = []
for i in range(1, 1000001):
    if isPrime(i): 
        bla.append(i)
        print(i)
#bla = [i for i in range(1,1000001) if isPrime(i)]
#print(bla)

bla = sorted(bla)
highest = 0
hinumber = 0
for i in range(len(bla)-1):
    count = 1
    number = bla[i]
    while number < 1000000:
        number += bla[i+count]
        #print(number)
        count += 1
        if isPrime(number) and count > highest: 
            hinumber = number
            highest = count
            print(hinumber, highest)


    



