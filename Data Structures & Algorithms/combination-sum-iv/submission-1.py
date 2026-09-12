class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()

        memo = { 0: 1}

        def dfs(total):
            if total in memo:
                return memo[total]
            
            res = 0
            for num in nums:
                if total < num:
                    break
                res += dfs(total - num)

            memo[total] = res
            return res
        
        return dfs(target)

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = {0: 1}
        for total in range(1, target + 1):
            
            dp[total] = 0
            for num in nums:
                dp[total] += dp.get(total - num, 0)
        
        return dp[target]