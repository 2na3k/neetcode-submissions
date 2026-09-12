# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         """
#         first, find all subarray
#         second, find sum and return that thing
#         -> rationale: since there is order (of finding subarray) -> finding subarray first, no doubt

#         or using 2 pointers
#         """
#         counter = 0
#         n = len(nums)

#         for i in range(n+1):
#             for j in range(i, n+1):
#                 if sum(nums[i:j]) == k:
#                     counter += 1
        
#         return counter



# class Solution:
#     "is the solution, but OOM"
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         res = 0
#         for i in range(len(nums)):
#             sum = 0
#             for j in range(i, len(nums)):
#                 sum += nums[j]
#                 if sum == k:
#                     res += 1
#         return res

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0
        prefixSums = { 0 : 1 }

        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return res