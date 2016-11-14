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
        
