num1 = 51
num2 = 102

while num2 != 0:
    temp = num2
    num2 = num1 % num2
    num1 = temp

print(num1)