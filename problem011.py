#Project Euler Problem #011:Largest product in a grid
#What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, diagonally) in the 20x20 grid?

def checkAll(grid, length):
    ret = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            currentProduct = 1
            #Check horizontal
            if x + length < len(grid[y]):
                for i in range(length):
                    currentProduct *= grid[y][x + i]
                if currentProduct > ret: ret = currentProduct
            currentProduct = 1
            #check vertical
            if y + length < len(grid):
                for i in range(length):
                    currentProduct *= grid[y + i][x]
                if currentProduct > ret: ret = currentProduct
            currentProduct = 1
            #check diagonal right down
            if y + length < len(grid) and x + length < len(grid[y]):
                for i in range(length):
                    currentProduct *= grid[y + i][x + i]
                if currentProduct > ret: ret = currentProduct
            currentProduct = 1
            #check diagonal left down
            if y + length < len(grid) and x - length > 0:
                for i in range(length):
                    currentProduct *= grid[y + i][x - i]
                if currentProduct > ret: ret = currentProduct
            #print(x,y,ret,sep=',')
    return ret

f = open("problem_data/p011_grid.txt",'r')
grid_lines = f.read().split("\n")
grid = []
for i in range(20):
    new = []
    for j in range(20):
        new.append(int(grid_lines[i].split(" ")[j]))
    grid.append(new)

print(checkAll(grid, 4))
