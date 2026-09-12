class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # "lower bound binary search"
        # l, r = 0, len(nums)

        # while l < r:
        #     m = l + ((r - l) // 2)
        
        # cheapest solution
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        
        return len(nums)
