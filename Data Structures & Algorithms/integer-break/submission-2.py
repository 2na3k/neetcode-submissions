class Solution:
    def integerBreak(self, n: int) -> int:
        def dfs(num, i):
            if min(num, i) == 0:
                return 1

            if i > num:
                return dfs(num, num)

            return max(i * dfs(num - i, i), dfs(num, i - 1))

        return dfs(n, n - 1)



class Solution:
    def integerBreak(self, n: int) -> int:
        # top down, breaking the things from n to something something idk fuck that
        dp = {}

        def dfs(num, i):
            if min(num, i) == 0:
                return 1
            
            if (num, i) in dp:
                return dp[(num, i)]
            
            if i > num:
                dp[(num, i)] = dfs(num, num)
                return dp[(num, i)]
            

            dp[(num, i)] = max(
                i * dfs(num - i, i), dfs(num, i - 1)
            )
            return dp[(num, i)]
        
        return dfs(n, n-1)

class Solution:
    # bottom up
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1

        for num in range(2, n +1):
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                dp[num] = max(dp[num], dp[i] * dp[num-i])
        
        return dp[n]
        