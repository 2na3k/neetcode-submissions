class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # natural solution


        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # out = [[None] * n] * m # guess that's fine OH SHIT THAT'S NOT WORK
        out = [[None for _ in range(n)] for _ in range(m)] # -> must do this

        # need to deal with this -> move whatever
        directions = [(1, 0), (0, 1)]
        
        def dfs(i, j) -> int:
            # this will dynamically update the out mat too
            # print(i, j)
            # print(out)
            
            if i >= m or j >= n or obstacleGrid[i][j]:
                return 0 # out of bound

            if i == (m - 1) and j == (n - 1):
                return 1
            
            if out[i][j] is not None:
                return out[i][j]

            res = 0
            for di, dj in directions:
                res += dfs(i + di, j + dj)
            
            out[i][j] = res
            return res

        return dfs(0,0)