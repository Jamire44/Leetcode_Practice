nums = [1,1,1,2,2,3,9,9,9,9,9,9,9]
k = 2

maxedOne = 0
freq = {}
for i, num in enumerate(nums):
    freq[num] = freq.get(num, 0) + 1

for key in freq:
    maxed = max(maxedOne, freq[key])
    



print(freq)