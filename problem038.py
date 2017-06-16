#!/usr/bin/env python3
#Project Euler problem #038: Pandigital multiples

def isPandigital(strnum):
    if len(set(strnum)) == 9: 
        return True
    return False


arr = []
for n in range(2, 10):
    print(n)
    limit = int(int('9'*(int(9/n) + 2))/n + 2) 
    for num in range(1, limit):
        zahl = ''
        for i in range(1, n):
            zahl += str(i*num)
        if '0' not in zahl and len(zahl) == 9 and isPandigital(zahl):
            arr.append(int(zahl))



print(arr)
print(max(arr))
