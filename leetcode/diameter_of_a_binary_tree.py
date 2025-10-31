class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfTree(root: TreeNode):
    largest_diameter = 0

    def height(root):
        if root is None:
            return 0
        
        left_height = height(root.left)
        right_height = height(root.right)
        diameter = left_height + right_height

        largest_diameter = max(largest_diameter, diameter)

        return 1 + max(left_height, right_height)
    
    height(root)
    return largest_diameter
