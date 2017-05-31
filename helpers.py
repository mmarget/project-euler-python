def isPrime ( i ):
    if i == 1: return False
    if i == 2: return True
    c = 2
    ret = True
    while c < (pow(i,0.5)+1):
        if i % c == 0:
            ret = False
            break
        c = c + 1
    return ret

def rotate(arr):
    ret = []
    first = arr[0]
    for i in range(len(arr) - 1):
        ret.append(arr[i+1])
    ret.append(first)
    return ret

def lexicographicPermutation(arr):
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False
    
    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    
    # Reverse suffix
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    return True

def arrToInt(arr):
    ret = ''
    for i in range(len(arr)):
        ret = ret + str(arr[i])
    return int(ret)

def intToArr(i):
    istr = str(i)
    ret = []
    for j in range(len(istr)):
        ret.append(int(istr[j]))
    return ret
        
