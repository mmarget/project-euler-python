#!/usr/bin/env python3
#Project Euler Problem #023: non-abundant sums


def find_divisors(n):
    arr = [1]
    for i in range(2, (int(n**0.5)+1)):
        if n % i == 0:
            arr.append(i)
            arr.append(int(n/i))
    return sorted(list(set((arr))))



def find_abundand_nums(limit):
    arr = []
    for i in range(1, limit+1):
        if sum(find_divisors(i)) > i: arr.append(i)
    return arr


anums = find_abundand_nums(28123)
bla = list(set([i+j for i in anums for j in anums if i+j <= 28123]))
print(sum([i for i in range(1, 28124) if i not in bla]))
