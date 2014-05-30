import math

primeIndex = 1
num = 3
notDone = True
while notDone:
    flag = True
    for j in range(2,int(math.floor(math.sqrt(num)))+1): #ceil because range must be upper bound + 1
        if num % j == 0:
            flag = False
    if flag:
        primeIndex += 1
    if primeIndex == 10001:
        notDone = False
    else:
        num += 2
print num
