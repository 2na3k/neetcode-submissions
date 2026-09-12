class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # always 2 pointers
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)



    def isSubsequence(self, s: str, t: str) -> bool:
        def dfs(i, j):
            if i == len(s):
                return True
            if j == len(t):
                return False

            if s[i] == t[j]:
                return dfs(i + 1, j+ 1)
            return dfs(i, j + 1)
        
        return dfs(0, 0)