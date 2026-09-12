class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = "", 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                l, r = i, j
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1

                if l >= r and resLen < (j - i + 1):
                    res = s[i : j + 1]
                    resLen = j - i + 1
        return res

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ridx = 0
        rlen = 0

        for i in range(len(s)):
            l, r = i, i

            # odd len
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > rlen:
                    ridx = l
                    rlen = r - l + 1
                l -= 1
                r += 1

            # even len
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > rlen:
                    ridx = l
                    rlen = r - l + 1
                l -= 1
                r += 1
        
        return s[ridx: ridx + rlen]