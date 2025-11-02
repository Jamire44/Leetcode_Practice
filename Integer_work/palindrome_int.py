num = 1221
original = num
reverse = 0

while original != 0:
    digit = original % 10
    reverse = reverse * 10 + digit
    original //= 10

if num == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")