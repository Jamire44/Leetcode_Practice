def max_root(root):
    if not root: return 0
    return 1 + max(max_root(root.left), max_root(root.right))