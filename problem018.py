#Project Euler Problem #018: Maximum path sum I
#Find the maximum total from top to bottom of problem_data/p018_data.txt, you can only move to adjacent numbers, when viewing as a pyramid

def printPyramid(pyramid):
    for i in range(len(pyramid)):
        print(pyramid[i])   
    
f = open("problem_data/p018_data.txt",'r')
pyramid_lines = f.read().split("\n")
#print(pyramid_lines[0].split(" "))
pyramid = []
for i in range(len(pyramid_lines) - 1):
    new = []
    for j in range(len(pyramid_lines[i].split(" "))):
        new.append(int(pyramid_lines[i].split(" ")[j]))
    pyramid.append(new)
 
for y in range(len(pyramid) - 1):
    for x in range(len(pyramid[y])):
        if x == 0: pyramid[y + 1][x] += pyramid[y][x]
        if x < len(pyramid[y]) - 1 and pyramid[y][x] <= pyramid[y][x + 1]:pyramid[y + 1][x + 1] += pyramid[y][x + 1] 
        if x < len(pyramid[y]) - 1 and pyramid[y][x] > pyramid[y][x + 1]:pyramid[y + 1][x + 1] += pyramid[y][x]
        if x == len(pyramid[y]) - 1: pyramid[y + 1][x + 1] += pyramid[y][x]

printPyramid(pyramid)
print("max path sum is:",max(pyramid[len(pyramid) - 1]))
