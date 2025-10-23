from collections import Counter

s = "loveleetcode"

def countering(s):
    count = Counter(s)
    for i, chr in enumerate(s):
        if count[chr] == 1:
            return i
        
print(countering(s))