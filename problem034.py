# Project Euler Problem 34: Digit factorials
# 145 is a curious number, as 1! + 4! + 5! = 145
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
import math 

def digitFactorialSum(n):
    factorialSum = 0
    if n < 3: return factorialSum
    nstr = str(n)
    for i in range(len(nstr)):
        factorialSum += math.factorial(int(nstr[i]))
    return factorialSum

allSum = 0
for i in range(100000000):
    dfs = digitFactorialSum(i)
    if dfs == i:
        allSum += dfs
        print(dfs, allSum)

