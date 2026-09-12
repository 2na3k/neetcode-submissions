# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        def traverse(rt):
            if not rt:
                return None
            traverse(rt.left)
            out.append(rt.val)
            traverse(rt.right)
        
        traverse(root)
        return out    