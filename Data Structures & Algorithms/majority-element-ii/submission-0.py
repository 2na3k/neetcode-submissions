class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # again, same algo
        # Bernoulli ones, the final out can have max 2 ones

        out = []
        rep_set = {}
        threshold = len(nums) // 3
        
        for n in nums:
            if n in rep_set:
                rep_set[n] += 1
            else:
                rep_set[n] = 1
        
        for k, v in rep_set.items():
            if v > threshold:
                out.append(k)

        
        return out
        