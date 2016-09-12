#Project Euler Problem #017: Number letter counts
#If all the numbers from 1 to 1000 inclusive were written out in words, how many letters would be used (not counting spaces or hyphens)?
#NOTE: not finished

def intToText(i):
    ret = ''
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eightteen', 'nineteen']
    tens = ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if len(str(i)) == 4:
        ret = "onethousand"
    elif len(str(i)) == 3:

