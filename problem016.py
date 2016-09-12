#Euper Project Problem016: Power digit sum
#What is the sum of the digits of the number 2^1000

largeNum = 2**1000
largeChar = str(largeNum)
print(largeChar)
sum = 0
for i in range(len(largeChar)):
    sum = sum + int(largeChar[i])
print(sum)
