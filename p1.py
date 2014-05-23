def tilstax(x,y):
    sum = 0
    i = 1
    while x*i < 1000:
        sum += x*i
        i += 1
    i = 1
    while y*i < 1000:
        if y*i % x != 0:
            sum += y*i
        i += 1
    return sum

print tilstax(3, 5)
