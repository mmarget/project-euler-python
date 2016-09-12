#euler problem #015: Lattice paths
#How many different routes are there for a 20x20 grid when starting at the top left and finishing at the bottom right, when only moving down and right
#NOTE: very inefficient code, basically brute forcing the problem, works fine for smaller grids up to ~12x12, will take a very long time for 20x20. solution however is in the last line, for n*m grid, it is (n+m)!/(n!*m!) 
import math
def checkForGoal(n):
    kiff = str(bin(n))[2:].zfill(10)
    a, b = 0, 0
    ret = False
    #print(kiff)
    for i in range(len(kiff)):
        if kiff[i] == '0':
            a += 1
        elif kiff[i] == '1':
            b += 1
        else: 
            print("error")
    if a == b:
        ret = True
    return ret

#i = 1099511627775
i=int('1111111111', 2)
#print(str(bin(i)).zfill(4))
#print(kiff, len(kiff))
count = 0
while i > 0:
    foo = checkForGoal(i)
    print(str(bin(i))[2:].zfill(10),foo,count)
    if foo == True:
        count += 1
    
    #print(str(bin(i)),foo,count)
    i -= 1
print(count)
print(math.factorial(2*20)/(math.factorial(20))**2)
