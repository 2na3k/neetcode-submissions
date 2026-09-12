class Solution:
    def numSquares(self, n: int) -> int:
        def dfs(target):
            if target == 0:
                return 0

            res = target
            for i in range(1, target):
                if i * i > target:
                    break
                res = min(res, 1 + dfs(target - i * i))
            return res

        return dfs(n)


# class Solution:
#     def numSquares(self, n: int) -> int:
#         memo = {}

#         def dfs(target):
#             print(f"target={target}")
#             if target == 0:
#                 return 0
#             if target in memo:
#                 return memo[target]

#             res = target
#             for i in range(1, target + 1):
#                 if i * i > target:
#                     break
#                 res = min(res, 1 + dfs(target - i * i))

#             memo[target] = res
#             return res

#         return dfs(n)

class Solution:
    def numSquares(self, n: int) -> int:
        # technically still failed due to recursion depth limit
        # bottom up 1
        memo = {}

        def dfs(target):
            if target == 0:
                return 0
            if target in memo:
                return memo[target]

            res = target
            for i in range(1, target + 1):
                if i * i > target:
                    break
                res = min(res, 1 + dfs(target - i * i))

            memo[target] = res
            return res
        return dfs(n)


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target - square])

        return dp[n]













