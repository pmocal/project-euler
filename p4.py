def isPalindrome(x):
	digits = []
	temp = x
	while temp > 0:
		digits.append(temp % 10)
		temp = temp // 10
	numDigits = len(digits)
	for d in range(0,numDigits/2):
		flag = (digits[d] == digits[numDigits - 1 - d])
		if flag == False:
			return flag
	return True

maxP = 0
for i in range(100,1000):
    for j in range(100,1000):
        if isPalindrome(i*j) and i*j > maxP:
			maxP = i*j

print maxP