class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ref = {}
        for i in nums:
            if ref.get(i, None) is None:
                ref[i] = 1
            else:
                return True
        
        return False
