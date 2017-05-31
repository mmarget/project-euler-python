#Project Euler Problem #007: 100001st prime
#What is the 10001st prime number?

def isPrime ( i ):
    c = 2
    ret = True
    while c < (i**0.5) + 1:
        if i % c == 0:
            ret = False
            break
        c = c + 1
    return ret

count = 1
i = 2
while count < 10001:
    if isPrime(i) == True:
        count = count + 1
        print(count, " : ",i)
    i = i + 1
