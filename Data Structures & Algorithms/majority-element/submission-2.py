class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = len(nums) // 2

        rep_set = {}
        
        for n in nums:
            if n in rep_set:
                rep_set[n] += 1
            else:
                rep_set[n] = 1
        for k, v in rep_set.items():
            if v > threshold:
                return k
        
        return None