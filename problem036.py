#!/usr/bin/env python3
#Project Euler Problem #036: Double-base palindromes
#find the sum of all numbers less than 1 million which are palindromic in base 10 and 2.

print(8, str(bin(8)))

def is_palindrome(n):
    p = str(n)
    for i in range(len(p)):
        if p[i] != p[len(p) -1 -i ]: 
            return False
    return True
def is_palindrome_bin(n):
    p = str(bin(n))[2:]
    for i in range(len(p)):
        if p[i] != p[len(p) -1 - i]:
            return False
    return True

arr = []
for i in range(1000001):
    if is_palindrome(i) and is_palindrome_bin(i):arr.append(i)

print(sum(arr))

#print(is_palindrome(585), is_palindrome_bin(585))
