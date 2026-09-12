# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        """
        Idea:
        - comparing the value of the key to the root, then move the cursor
        - > < move the cursor, = then do the assignment
        - assignment: do anything for me
        """

        if key > root.val:
            # recursive move
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # equal, then fucking handle the move
            # I don't even understand this shit
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            cur = root.right

            while cur.left:
                cur = cur.left
            
            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)
        
        return root