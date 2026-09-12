class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # check
        n = len(nums)
        in_order, reverse = [1] * n, [1] * n

        for i in range(1, n):
            in_order[i] = in_order[i - 1] * nums[i-1]

        

        print("in order: ", in_order)

        for i in range(n - 2, -1, -1):
            reverse[i] = reverse[i + 1] * nums[i + 1]
        print("reverse: ", reverse)

        return [in_order[i] * reverse[i] for i in range(n)]