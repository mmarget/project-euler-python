def isPrime ( i ):
    c = 2
    ret = True
    while c < (pow(i,0.5)+1):
        if i % c == 0:
            ret = False
            break
        c = c + 1
    return ret
def rotate(i):
    numchar = str(i)
    first = numchar[0]
    ret = ''
    for j in range(len(numchar)-1):
        ret += numchar[j+1]
    ret += first
    i = int(ret)
    return i



