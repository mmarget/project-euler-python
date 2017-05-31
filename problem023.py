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

#print([i for i in find_abundand_nums(20000) if i%2 != 0])

#print(find_divisors(4))


anums = find_abundand_nums(28123)
arr = []
for number in range(1, 28124):
    value = True
    bla = [i for i in anums if i <= number]
    for i in bla:
        if value == False: break
        for j in bla:
            if i != j and i + j == number: 
                value = False
                break
    if value == True: 
        arr.append(number)
        print(number)

print( sum(arr))
