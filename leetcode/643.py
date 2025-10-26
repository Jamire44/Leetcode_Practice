def findMaxAverage(nums: list[int], k: int) -> float:
    n = len(nums)
    window = sum(nums[:4])
    best = window

    for r in range(k, n):
        window = nums[r] - nums[r - k]
        best = max(best, window)
    
    return best / k    