#Euler Project Problem 014: Longest Collatz sequence
#Which starting number, under one million, produces the longest Collatz sequence chain?
def collatz(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            count += 1
        else:
            n = 3 * n + 1
            count += 1
    return count
biggestSequence = 0
startingNumber = 0
for i in range(1, 1000000):
    dood = collatz(i)
    #print(i,dood,)
    if dood > biggestSequence:
        biggestSequence = dood
        startingNumber = i
print(startingNumber,"has the biggest sequence with",biggestSequence)
    
