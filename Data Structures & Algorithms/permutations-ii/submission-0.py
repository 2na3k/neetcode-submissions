class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        # yeah why not?
        res = set()

        def backtrack(perm):
            if len(perm) == len(nums):
                res.add(tuple(perm)) # need to be hashable
                return None
            
            # next, fuck the other ones

            for i in range(len(nums)):
                if nums[i] != float("-inf"):
                    perm.append(nums[i])
                    nums[i] = float("-inf")
                    backtrack(perm)
                    nums[i] = perm[-1]
                    perm.pop()
        
        backtrack([])

        return list(res)