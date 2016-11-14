# Project Euler Problem #041: Pandigital prime
#What's the largest n-digit pandigital prime that exists. Ex: 2143 is pandigital prime as it uses every number from 1 to 4

import helpers

arr = []
for i in range(1, 8):
    arr.append(i)

print(helpers.arrToInt(arr))
check = False
while helpers.lexicographicPermutation(arr):
    if helpers.isPrime(helpers.arrToInt(arr)):
            check = True
            print(helpers.arrToInt(arr))
#    helpers.lexicographicPermutation(arr)
