def moveZeroes(nums: list[int]) -> None:
    l = 0

    for r in range(len(nums)):
        if nums[r] != 0:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1

#           l
#               r
nums = [1,1,0,0,12]
moveZeroes(nums)
print(nums)