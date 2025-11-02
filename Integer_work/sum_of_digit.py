num = 9359
copy = num
sum = 0

while copy != 0:
    digit = copy % 10
    sum += digit
    copy //= 10

print(sum)