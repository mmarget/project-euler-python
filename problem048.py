#Project Python Problem #048: Self powers
#Find the last ten digits of the series 1^1 + 2^2 + 3^3 + ... + 1000^1000
sum = 0
for i in range(1, 1001):
    sum += i**i

summ = str(sum)
print(summ[len(summ)-10:])
