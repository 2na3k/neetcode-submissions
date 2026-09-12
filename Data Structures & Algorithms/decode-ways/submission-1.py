class Solution:
    def numDecodings(self, s: str) -> int:
        # must do the dynamic programming for fuck that
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            
            res = dfs(i+1)

            if i < len(s) - 1:
                if (
                    s[i] == '1' 
                    or (s[i] == '2' and s[i+1] < '7')
                ):
                    res += dfs(i+2)
            
            return res
        
        return dfs(0)


class Solution:
    def numDecodings(self, s: str) -> int:
        # yeah just the one above, but do differently
        
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0
            
            res = dfs(i+1)

            if i < len(s) - 1:
                if (
                    s[i] == '1' 
                    or (s[i] == '2' and s[i+1] < '7')
                ):
                    res += dfs(i+2)
            dp[i] = res
            return res
        
        return dfs(0)