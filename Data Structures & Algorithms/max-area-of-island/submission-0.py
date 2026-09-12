# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

#         visited = set()
#         res = []
#         rc, cc = len(grid), len(grid[0])

#         def dfs(i, j) -> int:
#             # out of grid, visited or not island -> skip yah
#             # must handle the case grid[i][j] == 0 since even the root is land, the sink is not
#             if (
#                     i < 0 or i >= rc or 
#                     j < 0 or j >= cc or 
#                     grid[i][j] == "0" or 
#                     (i, j) in visited
#                 ):
#                 return 0
            
#             visited.add((i, j))
            
#             return (
#                 dfs(i + 1, j)
#                 + dfs(i - 1, j)
#                 + dfs(i, j + 1)
#                 + dfs(i, j - 1)
#             )

#         for i in range(rc):
#             for j in range(cc) and (i, j) not in visited:
#                 res.append(dfs(i, j))

#         return max(res)

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        visited = set()
        res = []
        rc, cc = len(grid), len(grid[0])

        def dfs(i, j) -> int:
            # FIX 1: Integer comparison (0 instead of "0")
            if (
                i < 0 or i >= rc or 
                j < 0 or j >= cc or 
                grid[i][j] == 0 or 
                (i, j) in visited
            ):
                return 0
            
            visited.add((i, j))
            
            # FIX 2: Added `1 +` to include the current land cell
            return (
                1
                + dfs(i + 1, j)
                + dfs(i - 1, j)
                + dfs(i, j + 1)
                + dfs(i, j - 1)
            )

        for i in range(rc):
            for j in range(cc):
                # Only run DFS on unvisited land cells to keep res clean
                if grid[i][j] == 1 and (i, j) not in visited:
                    res.append(dfs(i, j))

        return max(res) if res else 0