#Project Euler Problem #027: Quadratic primes
#Find the product of the coefficients a and b for the quadratic expression(n^2+a*n+b) that produces the maximum number of primes for consecutive values of n, starting with n = 0, where |a|<=1000 and |b|<=1000
#Thoughts: b has to be positive and a prime number, otherwise the equation fails at n = 0

def isPrime ( i ):
    c = 2
    if i == 2 or i == 3:
        return True 
    if i <= 1:
        return False
    ret = True
    while c < (pow(i,0.5)+1):
        if i % c == 0:
            ret = False
            break
        c = c + 1
    return ret


def quadraticPrimeFunc(n, a, b):
    return ((n*n)+(a*n)+b)

def findQuadPrimes(lim_a, lim_b):
    a_max, b_max, n_max = 0, 0, 0
    for b in range(1, lim_b):
        if isPrime(b) == True:
            for a in range(-lim_a,lim_a):
                n = 0
                while isPrime(quadraticPrimeFunc(n, a, b)) == True:
                    n += 1
                if n > n_max:
                    n_max = n
                    b_max = b
                    a_max = a
                    print("a=",a,"b=",b,"n=", n)
    return {'a':a_max, 'b':b_max, 'n':n_max}

letsGo = findQuadPrimes(1000, 1000)
print(letsGo['a']*letsGo['b'])

