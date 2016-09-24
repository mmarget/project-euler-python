longString = ''
i = 0
while len(longString) < 1000000:
    i += 1
    longString += str(i)
f = int(longString[0]) * int(longString[9]) * int(longString[99]) * int(longString[999]) * int(longString[9999]) * int(longString[99999]) * int(longString[999999])
print(f)
