class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # fucking going whatever with that (i use dfs)

        rc, cc = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j):
            # base case
            if (i, j) in visited:
                return 0
            
            if i < 0 or j < 0 or i >= rc or j >= cc or grid[i][j] == 0:
                return 1
            
            visited.add((i, j))
            
            # the actual bound: check 4 edge(s) of the thing

            out = (
                dfs(i, j+1)
                + dfs(i+1, j)
                + dfs(i-1, j)
                + dfs(i, j-1)
            )
            return out
        
        # have to iterate through everything throughout this
        for i in range(rc):
            for j in range(cc):
                if grid[i][j]:
                    return dfs(i, j)
        return 0
            