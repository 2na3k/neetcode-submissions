# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs way

        def dfs(node, maxv):
            if not node:
                return 0
            
            res = 1 if node.val >= maxv else 0
            maxv = max(maxv, node.val)
            res += dfs(node.left, maxv)
            res += dfs(node.right, maxv)
            return res
        
        return dfs(root, root.val)


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # bfs way

        res = 0
        
        q = deque()
        q.append((root, -float('inf')))

        while q:
            node, maxv = q.popleft()
            if node.val >= maxv:
                res += 1
            
            if node.left:
                q.append((node.left, max(node.val, maxv)))
            
            if node.right:
                q.append((node.right, max(node.val, maxv)))

        return res