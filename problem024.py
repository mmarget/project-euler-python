#!/usr/bin/env python3

#Project Euler Problem #24: Lexicographic permutations
#What is the 1000000th lexiographic permutation of 0123456789

import helpers

arr = []
for i in range(10):
    arr.append(i)

for _ in range(999999):
    helpers.lexicographicPermutation(arr)
print(helpers.arrToInt(arr))
