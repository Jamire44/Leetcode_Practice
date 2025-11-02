nums = [0,1,0,3,12,0,0,45,245,0,0]

l = 0

for r in range(len(nums)):
    if nums[r] != 0:
        nums[r], nums[l] = nums[l], nums[r]
        l+=1

print(nums)