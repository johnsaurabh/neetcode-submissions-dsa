# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        good_node_count=0
        max_val=-100
        def dfs(node,max_val):
            nonlocal good_node_count
            if node is None:
                return 0

            if node.val>=max_val:
                good_node_count+=1
            max_val=max(max_val,node.val)
            dfs(node.left,max_val)
            dfs(node.right,max_val)

            return good_node_count
        
        dfs(root,max_val)

        return good_node_count



        