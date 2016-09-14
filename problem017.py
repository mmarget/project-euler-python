#Project Euler Problem #017: Number letter counts
#If all the numbers from 1 to 1000 inclusive were written out in words, how many letters would be used (not counting spaces or hyphens)?
#NOTE: not finished

def intToText(i):
    ret = ""
    numbers = {0:'',1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',10:'ten',11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}
    if len(str(i)) == 4:
        return "onethousand"
    if len(str(i)) == 3:
        ret += numbers[int((i - (i % 100))/100)] + "hundred"
        if i % 100 != 0:
            ret += "and"
    if i % 100 <= 20:
        ret += numbers[i % 100]
    if i % 100 > 20:
        ret += numbers[(i % 100) - (i % 10)] + numbers[i % 10]
    return ret

    
print(567 % 1000,int((567 - (567 % 100))/100))
print()
sum = 0
for i in range(1, 1001):
    text = intToText(i)
    sum += len(text)
    print(text, len(text))
print(sum)
