n = 0
sum = 0
num2 = 1
num1 = 0

while n <4000000:
    num1 = sum
    num2 = num1
    sum = num1+num2
    if n % 2 == 0:
        sum += n
print (sum)