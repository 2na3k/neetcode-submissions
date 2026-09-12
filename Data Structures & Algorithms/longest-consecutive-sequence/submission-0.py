# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         # sort then do the thing -> heaptify it then sliding windows
#         # let's do this in the hash set way

#         hs = set(nums)

#         print("hs: ", hs)
#         max_val = 0

#         for num in hs:
#             if num - 1 not in hs:
#                 length = 1
#                 while (num + length) in hs:
#                     length += 1
#                 max_val = max(length, max_val)
        
#         return max_val


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res