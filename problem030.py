#Project Euler Problem #030: Digit fifth powers
#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits

def findFifth(limit):
    l = []
    for i in range(2, limit + 1):
        charint = str(i)
        summ = 0
        for j in range(len(charint)): summ += int(charint[j])**5
        if summ == i: l.append(i)
    return l

print(findFifth(10000000))
print(sum(findFifth(1000000)))
