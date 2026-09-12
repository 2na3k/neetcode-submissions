class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1

        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if (i != j) and (nums[i] + nums[j] == target):
                    return sorted([i, j])
        