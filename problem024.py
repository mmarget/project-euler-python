#Project Euler Problem #24: Lexicographic permutations
#What is the 1000000th lexiographic permutation of 0123456789

def lexi(nmin, nmax, perm):
    number = []
    i = nmin
    while i <= nmax:
        number.append(i)
        i += 1
    for j in range(perm):
        for k in 
    return number

print(lexi(0, 9, 0))

