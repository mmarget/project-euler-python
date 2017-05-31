#Project Euler Problem #025: 1000-digit Fibonacci number
#What is the index of the first term in the Fibonacci sequence to contain 1000 digits
first = 1
second = 2
temp = 0
index = 3

while len(str(second)) < 1000:
    temp = second
    second = second + first
    first = temp
    index += 1
    print(index,len(str(second)))
print("The first number with 1000 digits is the",index,"th Fibonacci number",second)
