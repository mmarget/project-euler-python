#Project Euler Problem #010: Summation of primes
#Find the sum of all the Primes below 2m.

def isPrime ( i ):
    c = 2
    ret = True
    while c < (pow(i,0.5)+1):
        if i % c == 0:
            ret = False
            break
        c = c + 1
    return ret

sum = 5
i = 1
while ((i*6)-1) < 2000001:
    if isPrime((i*6)-1) == True:
        #print(i*6-1)
        sum = sum + (i*6)-1
    i = i + 1
i = 1
while (i*6+1) < 2000001:
    if isPrime((i*6)+1) == True:
        #print((i*6)+1)
        sum = sum + (i*6)+1
    i = i + 1
print(sum)
