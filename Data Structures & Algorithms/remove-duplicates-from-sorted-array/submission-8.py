# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         # should use fast and slow pointer
#         seen = set()
#         slow, fast = 0, 1
        
#         while slow < len(nums) - 1:
#             if nums[slow] == nums[fast]:
#                 nums = nums[:slow] + nums[slow+1:]
#             else:
#                 slow += 1
#                 fast += 1

#         print(f"final {nums}")
#         return len(nums)
    
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l