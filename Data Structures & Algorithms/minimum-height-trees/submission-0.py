class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # construct the graph
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # dfs, with node and parents
        def dfs(node, parent):
            hgt = 0
            for nei in adj[node]:
                if nei == parent:
                    continue
                hgt = max(hgt, 1 + dfs(nei, node))  # calculate the height of a tree
            return hgt

        minHgt = n  # max size could be when you flatten the tree
        res = []
        for i in range(n):
            curHgt = dfs(i, -1)
            if curHgt == minHgt:
                res.append(i)
            elif curHgt < minHgt:
                res = [i]
                minHgt = curHgt

        return res