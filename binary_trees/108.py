class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if not nums:
        return []
    
    mid = len(nums) // 2
    root = nums[nums[mid]]

    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])

sortedArrayToBST([-10,2,-5,0,19])



# if its odd, go length / 2 = 3
# even len / 2

#             i i+1
# -10, -3, 0, 5, 9


#  -10
# 
#
#
#
#