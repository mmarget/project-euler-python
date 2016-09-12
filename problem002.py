#Project Euler Problem #002: Even Fibonacci numbers
#Find the sum of all even Fibonacci sequence terms below 4m

first = 1
second = 2
temp = 0
sum = 0

while second < 4000000:
    if second % 2 == 0:
        sum = sum + second
    temp = second
    second = second + first
    first = temp
print("The sum of all even fibonacci terms below 4m equals ",sum)
