#Project Euler Problem #020: Factorial digit sum
#Find the sum of the digits in the number 100!

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

charbla = str(factorial(100))
sum = 0
for i in range(len(charbla)):
    sum = sum + int(charbla[i])
print("100!=",charbla)    
print("Sum of digits in 100!:",sum)
