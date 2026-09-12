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
            
            # first way to deal with that
            # root.val = cur.val
            # root.right = self.deleteNode(root.right, root.val)


            # second way

            cur.left = root.left
            res = root.right
            del root
            return res
        return root



class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        parent = None
        cur = root

        # find node to delete
        while cur and cur.val != key:
            parent = cur
            if key > cur.val:
                cur = cur.right
            else:
                cur = cur.left
        
        if not cur:
            return root


        # node with only one child or no child
        if not cur.left or not cur.right:
            child = cur.left if cur.left else cur.right
            if not parent:
                return child
            if parent.left == cur:
                parent.left = child
            else:
                parent.right = child
        
        else:
            par = None
            delNode = cur
            cur = cur.right
            while cur.left:
                par = cur
                cur = cur.left
            
            if par:
                par.left = cur.right
                cur.right = delNode.right
            
            cur.left = delNode.left

            if not parent:
                return cur
            
            if parent.left == delNode:
                parent.left = cur
            
            else:
                parent.right = cur
        return root

