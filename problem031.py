#Project Euler Problem #031: Coin sums
#How many different ways can 2Pounds be made using any number of coins (1p, 2p, 5p, 10p, 20p, 50p, 1P, 2P)

#values = [1,2,5,10,20,50,100,200]
#hiCoin = 0
#hiCoinCount = 0
count = 8
for i in range(200):
    print(i)
    print(count)
    for j in range(100):
        for k in range(40):
            for l in range(20):
                for m in range(10):
                    for n in range(4):
                        for o in range(2):
                            #for p in range(2):
                            if (i*1)+(j*2)+(k*5)+(l*10)+(m*20)+(n*50)+(o*100) == 200: count += 1
print(count)
    
