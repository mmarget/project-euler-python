#Project Euler Problem #006: Sum square difference
#Find the difference between the sum of the squares of the first one hundred natural numbers and the quare of the sum

sumOfSquares = 0
squareOfSums = 0
difference = 0
i = 0
while i <= 100:
    sumOfSquares = sumOfSquares + ( i * i )
    squareOfSums = squareOfSums + i
    i = i + 1
squareOfSums = squareOfSums * squareOfSums
print(squareOfSums," - ",sumOfSquares," = ",squareOfSums - sumOfSquares)

