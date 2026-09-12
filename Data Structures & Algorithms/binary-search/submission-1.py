# class Solution:
#     def binary_search(self, l: int, r: int, nums: list(int), target: int) -> int:
#         "recursive solution, would not suggest"
#         if l > r:
#             return -1
#         m = l + (r - l) // 2
#         if nums[m] == target:
#             return m
#         if nums[m] < target:
#             return self.binary_search(m + 1, r , nums, target)
#         return self.binary_search(l, m - 1, nums, target)
        
#     def search(self, nums: List[int], target: int) -> int:
#         return self.binary_search(0, len(nums) - 1, nums, target)

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:

#         # note: as index, left 0, and r must be len(n) - 1
#         l, r = 0, len(nums) - 1
        
#         while l <= r:

#             m = l + ((r- l) // 2)

#             if nums[m] > target:
#                 r = m - 1
#             elif nums[m] < target:
#                 l = m + 1
#             else:
#                 return m
#         return -1
        

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         # lower bound
#         l, r = 0, len(nums)

#         while l < r:
#             m = l + ((r - l) // 2)
#             if nums[m] >= target:
#                 r = m
#             elif nums[m] < target:
#                 l = m + 1
        
#         return l if (l < len(nums) and nums[l] == target) else -1



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        # upper bound
        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] >= target:
                r = m
            elif nums[m] < target:
                l = m + 1
        
        return r if (r < len(nums) and nums[r] == target) else -1