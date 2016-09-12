#Euler Project Problem #022: Name scores
#Name Score is determined by the sum of the respective Values of the letters in a name times its alphabetical position
#What is the total of all the name scores in the file (problem_data/p022_names.txt)?

alphabet = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26} #dict of values of the letters
            
#print(alphabet)

f = open ("problem_data/p022_names.txt", 'r')
names_full = f.read()
names_full = names_full.replace('\"', '')
names_split = names_full.split(",")
names_split = sorted(names_split, key= str.upper)
totalNameScore = 0
for i in range(len(names_split)):
    nameScore = 0
    for j in range(len(names_split[i])):
        nameScore += (alphabet[names_split[i][j]])

    totalNameScore += (nameScore * (i + 1))

print(totalNameScore)
