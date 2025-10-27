def maxArea(height: list[int]) -> int:

    n = len(height)
    l,r = 0, n-1
    best = 0

    while l < r:
        if height[l] < height[l+1]:
            l+=1

        if height[l] < height[r]:
            l+=1
        
        apart = r - l
        new_best = apart * height[r]
        best = max(best, new_best)
        r-=1

    return best

print(maxArea([1,2,1]))
#                    r
#                    l              
# Input: height = [1,2,1]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49