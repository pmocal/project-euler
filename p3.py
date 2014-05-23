num = 600851475143

import math

def largestpf(x):
    flag = 0
    for i in range(2,int(math.ceil(math.sqrt(x)))):
        if x % i == 0:
            flag = 1
    if flag == 0:
        return x
    for i in range(2,int(math.ceil(math.sqrt(x)))):
        if x % i == 0:
            return max(largestpf(x/i), largestpf(i))

print largestpf(num)

