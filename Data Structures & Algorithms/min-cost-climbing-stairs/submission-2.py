# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         # base case
        
#         # what if that shit is == 0? idk man just fucking skip that

#         n = len(cost)
#         if len(cost) == 1:
#             return cost[0]
#         if len(cost) == 2:
#             return min(cost)


#         mem = [cost[0], min(cost[0], cost[1])]
#         for i in range(2, n):
#             print(f"i={i}")
#             mem.append(min(mem[i - 2], mem[i - 1]) + cost[i])
        
#         return min(mem[-1], mem[-2])

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bottom up approach, not optimized
        def dfs(i):
            if i >= len(cost):
                return 0
            return cost[i] + min(dfs(i+1), dfs(i+2))
        
        return min(dfs(0), dfs(1))

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bottom up, from the index 0
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n+1):
            dp[i] = min(
                dp[i-1] + cost[i-1],
                dp[i-2] + cost[i-2]
            )
        
        return dp[n]