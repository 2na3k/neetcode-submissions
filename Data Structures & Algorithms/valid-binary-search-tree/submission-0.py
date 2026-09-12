# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # recursive first - DFS 
        # got it right but still dunno why it's wrong
        def is_valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            
            return is_valid(node.left, left, node.val) and is_valid(
                node.right, node.val, right
            )
            
        return is_valid(root, float("-inf"), float("inf"))