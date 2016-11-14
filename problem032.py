#!/usr/bin/env python3
#Project Euler Problem #032: Pandigital products
#Find the sum of all products whose multiplicand/multiplier/product idenfity can be written as a 1 through 9 pandigital (every digit betwen 1 and 9 are represent

import helpers as hlp

arr = []
for i in range(1,10):
    arr.append(i)
solutions = []

def checkPandig(arr):
    for i in range(1, len(arr) - 2):
        for j in range(i + 1, len(arr) - 3):
            if hlp.arrToInt(arr[0:i]) * hlp.arrToInt(arr[i:j]) == hlp.arrToInt(arr[j:len(arr)]):
                solutions.append(hlp.arrToInt(arr[j:len(arr)]))
test = True
while test:
    checkPandig(arr)
    test = hlp.lexicographicPermutation(arr)
    
print(sum(set(solutions)))
