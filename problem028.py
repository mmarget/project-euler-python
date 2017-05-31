#Project Euler Problem #028: Number spiral diaglonals
#Whats the sum of the numbers on the diagonals in a 1001x1001 spiral formed like this 5x5 spiral:
#   
#   21 22 23 24 25
#   20  7  8  9 10
#   19  6  1  2 11
#   18  5  4  3 12
#   17 16 15 14 13

def createMatrix(x, y):
    matrix = []
    for i in range(y):
        new = []
        for j in range(x):
            new.append('')
        matrix.append(new)
    return matrix

def spiral(size):
    m = createMatrix(size, size)
    #set starting points
    x = int((size - 1)/2)
    y, circles  = x, x
    m[y][x] = 1
    num = 1
    for i in range(1, circles + 1):
        x += 1
        num += 1
        m[y][x] = num
        for j in range((2 * i) - 1):
            y += 1
            num += 1
            m[y][x] = num
        for k in range(2 * i):
            x -= 1
            num += 1
            m[y][x] = num
        for l in range(2 * i):
            y -= 1
            num += 1
            m[y][x] = num
        for n in range(2 * i):
            x += 1
            num += 1
            m[y][x] = num

    return m

def printMatrix(m):
    for i in range(len(m)):
        print(m[i])

def diagonalSum(m):
    size = len(m)
    ret = -1 # -1 for compensating double counting of 1
    for i in range(size):
        ret += m[i][i]
        ret += m[i][size - i - 1]
    return ret
#printMatrix(spiral(1001)) #you probably don't want to do that
print(diagonalSum(spiral(1001)))
