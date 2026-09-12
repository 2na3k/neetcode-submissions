class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mem = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            if i == m - 1 or j == n - 1:
                return grid[i][j]
            
            if i >= m or j >= m:
                return float('inf') # for the comparison to be smh always like that
            
            if mem[i][j] != -1:
                return mem[i][j]
            
            mem[i][j] = grid[i][j] + min(
                dfs(i+1, j),
                dfs(i, j+1)
            )   # only 2 directions, 2 choices
            return mem[i][j]
        return dfs(0, 0)

# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])
#         dp = [[-1] * n for _ in range(m)]

#         def dfs(r, c):
#             if r == m - 1 and c == n - 1:
#                 return grid[r][c]
#             if r == m or c == n:
#                 return float('inf')
#             if dp[r][c] != -1:
#                 return dp[r][c]

#             dp[r][c] = grid[r][c] + min(dfs(r + 1, c), dfs(r, c + 1))
#             return dp[r][c]

#         return dfs(0, 0)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mem = [[None] * n for _ in range(m)]

        def dfs(i, j):
            # Invalid paths should never win the min comparison
            if i >= m or j >= n:
                return float("inf")

            # Only the exact destination is a base case
            if i == m - 1 and j == n - 1:
                return grid[i][j]

            if mem[i][j] is not None:
                return mem[i][j]

            mem[i][j] = grid[i][j] + min(
                dfs(i + 1, j),
                dfs(i, j + 1)
            )

            return mem[i][j]

        return dfs(0, 0)