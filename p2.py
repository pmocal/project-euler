L=4000000
x = 0
y = 1
sum = 0
while (L - (y + x)) >= 0:
    temp = x
    x = y
    y = temp + y
    if y%2==0:
        sum += y
print sum

