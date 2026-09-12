class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # technically dynamic programming + backtrack

        n = len(grid)   # square grid so idc
        visited = [[False] * n for _ in range(n)]   # kinda a fucking same grid

        def dfs(node, t):
            r, c = node # node is a set of r, c and the total time

            if min(r, c) < 0 or max(r, c) >= n or visited[r][c]:
                return 1000000

            if r == n-1 and c == n-1:
                return max(t, grid[r][c])
            visited[r][c] = True

            t = max(t, grid[r][c])
            res = min(
                dfs((r+1, c), t),
                dfs((r-1, c), t),
                dfs((r, c+1), t),
                dfs((r, c-1), t)
            )

            visited[r][c] = False
            return res

        return dfs((0, 0), 0)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        movesets = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        n = len(grid)
        visited = set([(0, 0)])
        pq = [(grid[0][0], 0, 0)]   # (value, r, c), and each time pop to check the min of grid[r][c], priority to get this one
        
        while pq:
            val, r, c = heapq.heappop(pq)
            if r == n - 1 and c == n - 1:
                return val
            
            for dr, dc in movesets:
                nr, nc = r + dr, c + dc

                if (
                    nr < 0 or nc < 0
                    or nr == n or nc == n
                    or (nr, nc) in visited
                ):
                    continue
                visited.add((nr, nc))
                heapq.heappush(pq, (max(val, grid[nr][nc]), nr, nc))
            
            