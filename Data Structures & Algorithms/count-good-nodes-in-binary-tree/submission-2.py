# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxv):
            if not node:
                return None
            
            res = 0
            if node.val >= maxv:
                res = 1
            
            maxv = max(maxv, node.val)

            res += dfs(node.left, maxv)
            res += dfs(node.right, maxv)

            return res

        return dfs(root, root.val)



class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)