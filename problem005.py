#Project Euler Problem #005: Smallest multiple
#What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?

def isDividable(k):
    l = 1
    ret = True
    while l < 20:
        if k % l != 0:
            ret = False
            break
        l = l + 1
    return ret
i = 20
found = False
foundNumber = 0
while found == False:
    #print(i)
    if isDividable(i) == True:
        found = True
        foundNumber = i
    i = i + 2
print(foundNumber)
