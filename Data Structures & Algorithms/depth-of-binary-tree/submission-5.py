# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         res = 0
#         def dfs(node):
#             if not node:
#                 return 0
#             left = dfs(node.left)
#             right = dfs(node.right)
#             return 1 + max(left, right)
#         res = dfs(root)
#         return res


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # try to do the iterative, dfs as a variation
        
        queue = [(root, 1)]
        res = 0

        while queue:
            node, depth = queue.pop()

            if node:
                res = max(res, depth)
                if node.left:
                    queue.append((node.left, depth + 1))
                if node.right:
                    queue.append((node.right, depth + 1))         

        return res
