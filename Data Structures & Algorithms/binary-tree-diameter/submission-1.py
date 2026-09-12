# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # res = 0

        # # i mean the idea is there but we need a separate ones
        # def dfs(node):
        #     if not node:
        #         return None
        #     dfs(node.left)
        #     dfs(node.right)

        # dfs(node)
        # return res

        res = 0
        if not root:
            return 0

        def max_h(node) -> int:
            if not node:
                return 0
            return 1 + max(max_h(node.left), max_h(node.right))

        left_h = max_h(root.left)
        right_h = max_h(root.right)
        dia = left_h + right_h

        sub = max(self.diameterOfBinaryTree(root.left),
                  self.diameterOfBinaryTree(root.right))
        return max(dia, sub)
