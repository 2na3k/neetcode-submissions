# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         # brute force, O(nlog(n))
#         n = c = len(nums)
#         res = 0
#         l = 0
#         while l < n:
#             for r in range(l, n):
#                 subarr = nums[l: r]
#                 print(subarr)
#                 sum_val = sum(subarr)
#                 len_val = len(subarr)
#                 if sum_val >= target and len_val <= c:
#                     c = len_val
#                     res+=1
#                 print(f"c={c}")
#             l += 1
#         return c if res > 0 else 0


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        res = float("inf")

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1

        return 0 if res == float("inf") else res