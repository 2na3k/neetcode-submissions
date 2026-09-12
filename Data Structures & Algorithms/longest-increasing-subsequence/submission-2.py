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