notdone = True
num = 20
while notdone:
    b = []
    for i in range(1,21):
        b.append(num % i == 0)
    if False in b:
        num += 20
    else:
        notdone = False
print num
