class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # fucking going whatever with that (i use dfs)
        # dfs guys, dfs

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

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # do the bfs for the sake of how i can do that
        rc, cc = len(grid), len(grid[0])
        visited = set()

        # kind of direction for showing how can we move
        # technically changing the axis of those things by add/subtract 1 from i, j or no change
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))
            out = 0

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (
                        nx < 0
                        or ny < 0
                        or nx >= rc
                        or ny >= cc
                        or grid[nx][ny] == 0
                    ):
                        out += 1
                    
                    elif (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                
            return out

        for i in range(rc):
            for j in range(cc):
                if grid[i][j] == 1:
                    return bfs(i, j)
        
        return 0

        
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rc, cc = len(grid), len(grid[0])
        
        res = 0
        for i in range(rc):
            for j in range(cc):
                if grid[i][j] == 1:
                    res += (i + 1 >= rc or grid[i+1][j] == 0)
                    res += (j + 1 >= cc or grid[i][j+1] == 0)
                    res += (i - 1 < 0 or grid[i-1][j] == 0)
                    res += (j - 1 < 0 or grid[i][j-1] == 0)
        
        return res









