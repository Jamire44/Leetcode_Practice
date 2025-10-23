arr = [1,2,3]

# Can be used as a stack

arr.append(4)
arr.append(5)
print(arr)

arr.pop()

print(arr)

# O(n)
arr.insert(1, 7)
print(arr)

# O(1)
arr[0] = 0
arr[3] = 4

print(arr)