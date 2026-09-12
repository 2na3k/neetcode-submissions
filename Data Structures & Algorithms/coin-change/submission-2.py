class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # try the bfs first
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            

            res = 1e9

            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))

            memo[amount] = res
            return res
        
        minc = dfs(amount)

        return -1 if minc >= 1e3 else minc



class Solution :
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1