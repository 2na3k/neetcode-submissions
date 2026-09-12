class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        visited = set()

        adj = [[] for _ in range(n)]
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node, par):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False

            return True
        return dfs(0, -1) and len(visited) == n

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        q = deque([(0, -1)])  # (current node, parent node)
        visit.add(0)

        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visit:
                    return False
                visit.add(nei)
                q.append((nei, node))

        return len(visit) == n
