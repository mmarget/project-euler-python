#!/usr/bin/env python3
#Project Euler Problem #012:Highly divisible tirangular number
#What is the value of the first triangle number to have over 500 divisors?

import math

def triangle (n):
    #ret = 0
    #for i in range(n + 1):
        #ret +
    return math.floor((n*(n+1))/2)

def dividers (m):
    count = 1
    i = 0
    while i < (m/2)+1:
        i += 1
        if m % i == 0:
            count += 1

    return count

##################

def dividerss(n):
    count = 0
    dividers = 1 
    while n % 2 == 0:
        count += 1
        n = n/2
    dividers = dividers * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n/p
        dividers = dividers * (count + 1)
        p += 2
    return dividers
'''
def splitfind(limit):
    n = 1
    lnum, rnum = 1, 1
    while lnum * rnum < limit:
        n += 1
        lnum = pro_solution(n)
        rnum = pro_solution(n + 1)
        print("triangle",n," has",lnum * rnum,"divisors")
    return n
#print(dividers(triangle(7)))
splitfind(1000)
'''
i = 0
test = 0
while True:
    i += 1
    tri = triangle(i)
    div = dividerss(tri)
    if div > test:
        test= div
        print("triangle",i,"=",tri,", has",div,"dividers")
    if div > 500:
        print("triangle",i,"=",tri,", has",div,"dividers")
        break
