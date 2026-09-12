# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         # okay do the bfs with one stack

#         stack = [root]
#         res = []

#         while stack:
#             # nah let this solution later


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        

        # dfs: based on the index of the level (list) to append the thing


        def dfs(node, depth):
            # depth would act like the index/location of the level in the res

            if not node:
                return None
            
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return res

# let's pull that from your ass
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([(root, 0)])

        while q:
            cur, depth = q.popleft()
            if cur:
                if depth == len(res):
                    res.append([])
                res[depth].append(cur.val)
                if cur.left:
                    q.append((cur.left, depth + 1))
                if cur.right:
                    q.append((cur.right, depth + 1))
        return res
                
            


























        
