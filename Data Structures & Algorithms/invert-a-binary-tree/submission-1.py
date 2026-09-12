# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # dfs
        
        def inverse(node):
            if not node:
                return None
            
            if node.left or node.right:
                tmp = node.left
                node.left = node.right
                node.right = tmp
            inverse(node.left)
            inverse(node.right)

        inverse(root)

        return root