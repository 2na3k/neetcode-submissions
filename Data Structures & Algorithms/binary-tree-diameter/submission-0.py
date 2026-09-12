# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         # what the fuck
#         if not root:
#             return 0

#         leftHeight = self.maxHeight(root.left)
#         rightHeight = self.maxHeight(root.right)
#         diameter = leftHeight + rightHeight
#         sub = max(self.diameterOfBinaryTree(root.left),
#                   self.diameterOfBinaryTree(root.right))
#         return max(diameter, sub)


#     def maxHeight(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))


# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         # dfs with recursive
#         res = 0

#         def dfs(root):
#             nonlocal res

#             if not root:
#                 return 0
#             left = dfs(root.left)
#             right = dfs(root.right)
#             res = max(res, left + right)

#             return 1 + max(left, right)
        
#         dfs(root)
#         return res

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # dfs without recursive
        
        stack = [root]
        m = {None: (0, 0)} # heretic as fuck
        
        while stack:
            node = stack[-1]

            if node.left and node.left not in m:
                stack.append(node.left)
            elif node.right and node.right not in m:
                stack.append(node.right)
            else:
                node = stack.pop()

                left_h, left_d = m[node.left]
                right_h, right_d = m[node.right]
                m[node] = (1 + max(left_h, right_h),
                           max(left_h + right_h, left_d, right_d))
        
        return m[root][1]
