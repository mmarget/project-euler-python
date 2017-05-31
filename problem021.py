#Project Euler Problem #021: Amicable numbers
#Find sum of all amicable numbers under 10000

def isAmicable(n):
    amicSum = 0
    amicSum2 = 0
    for i in range(1, n - 1):
        if n % i == 0:
            amicSum += i
    for j in range(1, amicSum - 1):
        if amicSum % j == 0:
            amicSum2 += j
    if amicSum2 == n and amicSum != amicSum2:
        return True
    else:
        return False

asdf = 0
for i in range(1, 10000):
    if isAmicable(i) == True:
        print(i,"is amicable")
        asdf += i
print("sum:",asdf)
