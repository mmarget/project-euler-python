#!/usr/bin/env python3
#Project Euler Problem #043: Sub-string sivisibility
from helpers import *
bla = [1023456789]
#for i in range(1234567890, 9876543211):
#    if sorted(list(str(i))) ==  ['0','1','2','3','4','5','6','7','8','9']:
#        bla.append(i)
        #print(i)
i = 1023456789
while i != 9876543210:
    ump = list(str(i))
    lexicographicPermutation(ump)
    i = int("".join(ump))
    #i = int("".join(lexicographicPermutation(list(str(i)))))
    bla.append(i)


#print(bla)
blub = []
for n in bla:
    if int(str(n)[1:4]) % 2 == 0 and int(str(n)[2:5]) % 3 == 0 and int(str(n)[3:6]) % 5 == 0 and int(str(n)[4:7]) % 7 == 0 and int(str(n)[5:8]) % 11 == 0 and int(str(n)[6:9]) % 13 == 0 and int(str(n)[7:10]) % 17 == 0:
        blub.append(n)
        print(n)

print(sum(blub))
