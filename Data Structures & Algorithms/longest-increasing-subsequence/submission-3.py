class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(i, j):
            if i == len(nums):
                return 0
            
            LIS = dfs(i + 1, j) # not include i

            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i)) # include i
            
            return LIS
        
        return dfs(0, -1)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # of course, first thing to optimize is cache

        n = len(nums)
        memo = [[-1] * (n + 1) for _ in range(n)]

        def dfs(i, j):
            if i == len(nums):
                return 0

            # check if we have anything in the cache memo
            if memo[i][j + 1] != -1:
                return memo[i][j + 1]
            
            LIS = dfs(i + 1, j) # not include i

            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i)) # include i
            
            # to cache
            memo[i][j + 1] = LIS
            return LIS
        
        return dfs(0, -1)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # of course, first thing to optimize is cache
        # then, optimize the cache size
        # memo = [[-1] * (n + 1) for _ in range(n)]
        n = len(nums)
        memo = [-1] * n

        def dfs(i):
            if memo[i] != -1:
                return memo[i]


            
            LIS = 1

            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    LIS = max(LIS, 1 + dfs(j))
            
            memo[i] = LIS
            return LIS
        
        return max(
            dfs(i) for i in range(n)
        )
