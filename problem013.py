#Euler Project Problem #013: Large sum
#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
##############################################################################################

f = open("problem_data/problem013.txt", 'r')
full_text = f.read() 
splitted_text = full_text.split("\n")
sum = 0

for i in range(len(splitted_text)-1):
    sum = sum + int(splitted_text[i])

print(str(sum)[:10])
