# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def rec(rt):
            if not rt:
                return None
            
            rec(rt.left)
            rec(rt.right)
            res.append(rt.val)
        
        rec(root)
        return res