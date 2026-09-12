class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # im not pretentious to fucking do an OOP-liked solution

        res = []
        def backtrack(perm, nums, pick):

            # match case 
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            
            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    backtrack(perm, nums, pick)
                    perm.pop()
                    pick[i] = False

        backtrack([], nums, [False] * len(nums))
        return res