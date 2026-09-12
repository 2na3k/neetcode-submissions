class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # the backtrack way: to imagine the whole tree first
        def backtrack(i, total):
            if i == len(nums):
                return  total == target

            return (backtrack(i + 1, total + nums[i]) +
                    backtrack(i + 1, total - nums[i]))

        return backtrack(0, 0)
    

class Solution:
    # evolution mode: backtrack with cache
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mem = {}

        def backtrack(i, total):
            """
            i: index of the thing in the nums
            total: acc sum to compare
            """
            if i == len(nums):
                return total == target
            
            if (i, total) in mem:
                return mem[(i, total)]
            res = (
                backtrack(i + 1, total + nums[i]) +
                backtrack(i + 1, total - nums[i])
            )
            
            mem[(i, total)] = res
            return res
        return backtrack(0, 0)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # reduce the complexity of the cache
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+1)] # create a n + 1 * n + 1 array 

        dp[0][0] = 1
        
        for i in range(n):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count

        return dp[n][target]