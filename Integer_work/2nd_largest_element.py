nums = [12, 35, 54, 100, 1, 10, 34, 100]
copy = nums

first_largest = max(nums)
copy.remove(first_largest)
second = max(copy)
print(second)