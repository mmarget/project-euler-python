#Project Euler Problem #004: Largest palindrome product
#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(product):
    ret = True
    strprod = str(product)
    k = 0
    strlen = len(strprod)
    #print(strlen)
    while k < strlen and k < (strlen -1 -k):
        if strprod[k] != strprod[strlen - 1 - k]:
            ret = False
        k = k + 1
    return ret

#startingnumbers
i = 100
j = 100
largestPal = 0
product = 0
while i < 1000:
    while j < 1000:
        if isPalindrome(i*j) == True and i*j > largestPal:
            largestPal = i * j
        j = j + 1
    i = i + 1
    j = i

print("Largest product of 2 3-digit numbers is",largestPal)
