# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        """
        left -> right -> take the most left

        -> idea is taking the same level as a stack -> pop the final one for each level

        BFS, to pop the shit out of the thing
        """
        res = []
        
        def bfs(node, level):
            nonlocal res
            
            if not node:
                return None
            
            if len(res) <= level:
                res.append([])  # it should be more than the index (since we use level as index)
            
            # no overflow here so just fucking do it
            res[level].append(node.val)

            # recursive
            bfs(node.left, level + 1)
            bfs(node.right, level + 1)
        
        bfs(root, 0)

        # transform the res into new res
        out = [level[-1] for level in res]
        return out
    

# let's pull that from your ass
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # just need the top solution to fucking be flattened
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
        out = [level[-1] for level in res]
        return out
    






















