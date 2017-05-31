#!/usr/bin/env python3
#Project Euler Problem #044: Pentagon numbers

pen_numbers = []
for i in range(1, 50000):
    pen_numbers.append(int(i*(3*i-1)/2))
print(pen_numbers)
test = 0
pen_num_rem = list(pen_numbers)
for i in pen_numbers:
    print(i)
    pen_num_rem.remove(i)
    for j in pen_num_rem:
        if test == 0 or abs(i-j) < test: 
            if (i + j in pen_numbers) and (abs(i - j) in pen_numbers):
                test = abs(i-j)
                print("D:", test, "by numbers:", i, j)

print(test)


