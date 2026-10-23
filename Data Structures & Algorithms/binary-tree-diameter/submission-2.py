# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter=0

        def max_depth(root):
            nonlocal diameter 
            if not root:
                return 0
            left_depth=max_depth(root.left)
            right_depth=max_depth(root.right)
            diameter=max(diameter,left_depth+
            right_depth)
            return 1+ max(left_depth,right_depth)

        max_depth(root)
        return diameter