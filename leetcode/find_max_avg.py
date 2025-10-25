def findMaxAvg(nums: list[int], k: int) -> float:
    n = len(nums)
    curr_sum = 0

    for i in range(k):
        curr_sum += nums[i]
    
    max_av = curr_sum / k

    for i in range(k, n):
        curr_sum += nums[i]
        curr_sum -= nums[i-k]

        avg = curr_sum / k
        max_av = max(max_av, avg)
    
    return max_av
    
