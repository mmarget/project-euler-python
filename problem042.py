#!/usr/bin/env python3
#Project Euler Problem #042: Coded triangle numbers

f = open("problem_data/p042_words.txt", "r")
words = [word.replace("\"", "").lower() for word in f.read().split(",")]

trinums =[]
for i in range(1, 1000):
    trinums.append(int(i*(i+1)/2))

tri_words = []

for word in words:
    if sum([ord(char) - 96 for char in list(word)]) in trinums: tri_words.append(word)
print(tri_words, len(tri_words))

#ord(char) - 96
