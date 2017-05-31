#!/usr/bin/env python3
#project euler problem #045: triangular, pentagonal, and hexagonal
tri_num = []
pent_num = []
hex_num = []
for i in range(1, 100000):
    tri_num.append(int(i*(i+1)/2))
    pent_num.append(int(i*(3*i-1)/2))
    hex_num.append(int(i*(2*i-1)))

bla = [i for i in tri_num if i in pent_num]
print(bla)
blub = [i for i in bla if i in hex_num]
print(blub)

