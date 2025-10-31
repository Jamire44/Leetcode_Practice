a, b = 545467, 5454382

i = 0

while i < len(str(a)) and i < len(str(b)) and str(a)[i] == str(b)[i]:
    i+=1
print(sum(a)[:i])