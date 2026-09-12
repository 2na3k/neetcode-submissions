# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def dfs(rt):
            if not rt:
                return None

            res.append(rt.val)
            dfs(rt.left)
            dfs(rt.right)

        dfs(root)
        return res