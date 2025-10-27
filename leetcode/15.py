def threeSum(nums: list[int]) -> list[list[int]]:
    
    nums = set([])
    n = len(nums)
    l,m,r = 0,1,2

    while r <= n-1:
        if nums[l] != nums[m] and nums[l] != nums[r] and nums[m] != nums[r] and nums[l] + nums[m] + nums[r] == 0:
            nums.add([nums[l], nums[m], nums[r]])
        
    return nums

print(threeSum([-1,0,1,2,-1,-4]))

#                    r
#                   m
#                 l
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.