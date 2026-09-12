class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # def max_len_substring_from_pos(s: str, i: int):
        #     max_range = 1
        #     for i in range(len(s) - i - 1):
        #         print("the position", s[i])
        #         print("next one", s[i+1])
        #         if s[i + 1] not in s[:i + 1]:
        #             max_range += 1
        #     return max_range

        # def max_len_substring_from_pos(s: str, i: int):
        #     max_range = 1
        #     for i in range(1, len(s) - i):
        #         print("the position:", s[i])
        #         print("the string s[:i]: ", s[:i])
        #         print("bool result", (True if s[i] not in s[:i] else False))
        #         if s[i] not in s[:i]:
        #             max_range +=1
        #         print("max range: ", max_range)
        #     return max_range

        # maxOne = 0
        # for i in range(1, len(s)):
        #     maxOne = max(maxOne, max_len_substring_from_pos(s, i))

        # return maxOne

        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res