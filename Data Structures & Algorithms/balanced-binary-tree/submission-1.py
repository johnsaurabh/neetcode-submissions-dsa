# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        
        
        def height(node):

            if node is None:
                return (0,True)

            is_balanced=True

            left_height,left_balanced=height(node.left)
            right_height,right_balanced=height(node.right)
            tree_height=1+max(left_height,right_height)

            if abs(left_height-right_height)>1 or not left_balanced or not right_balanced:
                is_balanced=False

            return (tree_height,is_balanced)
        tree_height,is_balanced=height(root)
        return is_balanced

        