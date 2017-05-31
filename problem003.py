#Project Euler Problem #003: Largest prime factor
#What is the largest prime factor of the number 600851475143

cunt = 600851475143
i = 1
largestPrime = 0
def isPrime ( i ):
    c = 2
    ret = True
    while c < (i**0.5) + 1:
        if i % c == 0:
            ret = False
            break
        c = c + 1
    return ret

while i < (cunt**0.5)+1:
    if (isPrime(i) == True) and (cunt % i == 0):
        largestPrime = i
        #print("New largest prime is ",largestPrime)
    #print(i)
    i = i + 1

print("The largest Prime of",cunt,"is:",largestPrime)

