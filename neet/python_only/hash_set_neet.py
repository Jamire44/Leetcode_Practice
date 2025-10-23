mySet = set()

mySet.add(3)
mySet.add(5)
print(mySet)
print(1 in mySet)

# Constant time
mySet.remove(3)
print(2 in mySet)

# Set comprehension
mySet1 = {i for i in range(5)}
print(mySet1)
