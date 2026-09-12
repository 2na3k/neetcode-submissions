class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # always try the DFS first since this would do like:
        # if grid[i][j] == 1 then do the dfs
        # try one way with DFS, then deal with the other

        rn, cn = len(grid), len(grid[0])
        res = 0
        visited = set()

        def dfs(i, j) -> int:
            if (i, j) in visited:
                return 0
            
            visited.add((i, j))
            if (
                dfs() > 0  or dfs() > 0 or dfs() > 0 or dfs() > 0
            ):
                return 1
            return 0


        
        for i in range(rn):
            for j in range(cn):
                if gird[i][j] == 1:
                    res += dfs(i, j)
        
        return res


            


            
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rn, cn = len(grid), len(grid[0])
        res = 0

        def dfs(i: int, j: int) -> None:
            # Base case: out of bounds or current cell is water ("0")
            if i < 0 or i >= rn or j < 0 or j >= cn or grid[i][j] == "0":
                return
            
            # Mark the land as visited by "sinking" it
            grid[i][j] = "0"
            
            # Explore all 4 orthogonal directions
            dfs(i + 1, j)  # Down
            dfs(i - 1, j)  # Up
            dfs(i, j + 1)  # Right
            dfs(i, j - 1)  # Left

        # Iterate through every cell in the grid
        for i in range(rn):
            for j in range(cn):
                # Found unvisited land
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)  # Sink the entire island
        
        return res