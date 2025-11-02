nums = 1234
rev = 0
n = nums

while n != 0:
    digit = n % 10
    rev = rev * 10 + digit
    n//=10

print(n)