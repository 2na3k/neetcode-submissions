class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(nums):
            r1, r2 = 0, 0
            
            for n in nums:
                nr = max(r1 + n, r2)
                
                # move the pointer
                r1 = r2
                r2 = nr
            return r2
        
        return max(
            nums[0],
            dp(nums[1:]),   # skip the first one
            dp(nums[:-1])   # or skip the last one
        )