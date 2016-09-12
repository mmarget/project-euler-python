#Project Euler Problem #001: Multiples of 3 and 5
#Find the sum of all multiples of 3 or 5 below 1000

i = 1
summ = 0
while i < 1000:
    if (i % 3 == 0) or (i % 5 == 0):
        summ = summ + i
    i = i + 1
print("The sum of all multiples of 3 and 5 below 1000 is ",summ)
