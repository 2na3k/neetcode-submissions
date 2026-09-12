class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        for i in range(len(nums)):
            cur = nums[i]
            res = max(res, cur)
            for j in range(i + 1, len(nums)):
                cur *= nums[j]
                res = max(res, cur)

        return res


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cmin, cmax = 1, 1

        for num in nums:
            tmp = cmax * num
            cmax = max(num * cmax, num * cmin, num)
            cmin = min(tmp, num * cmin, num)
            res = max(res, cmax)
        return res