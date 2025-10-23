myMap = { "alice": 90, "bob": 70}
for key in myMap:
    print(key, myMap[key])

# If you dont even need key
for val in myMap.values():
    print(val)

# More concise as original loop
for key, val in myMap.items():
    print(key, val)