
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # natural solution

        # out = [[None] * n] * m # guess that's fine
        out = [[None for _ in range(n)] for _ in range(m)]

        # need to deal with this -> move whatever
        directions = [(1, 0), (0, 1)]
        
        def dfs(i, j) -> int:
            # this will dynamically update the out mat too
            # print(i, j)
            # print(out)
            

            if i == (m - 1) and j == (n - 1):
                return 1
            
            if i >= m or j >= n:
                return 0 # out of bound

            if out[i][j] is not None:
                return out[i][j]

            res = 0
            for di, dj in directions:
                res += dfs(i + di, j + dj)
            
            out[i][j] = res
            return res

        return dfs(0,0)