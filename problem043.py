#!/usr/bin/env python3
#Project Euler Problem #043: Sub-string sivisibility
bla = []
for i in range(1234567890, 9876543211):
    if sorted(list(str(i))) ==  ['0','1','2','3','4','5','6','7','8','9']:
        bla.append(i)
        print(i)

print("bla")
