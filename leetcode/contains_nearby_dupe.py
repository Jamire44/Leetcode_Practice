def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    window = set()

    for i, num in enumerate(nums) :
        if num in window:
            return True
        
        window.add(num)

        if len(window) > k:
            window.remove(nums[i-k])
        
    return False



print(containsNearbyDuplicate([1,2,3,1], 3))
print(containsNearbyDuplicate([1,0,1,1], 1))
print(containsNearbyDuplicate([1,2,3,1,2,3], 2))