class Solution:
    def climbStairs(self, n: int) -> int:
        hash_set = {}

        def rec(num):
            if hash_set.get(num, None):
                return hash_set[num]
            
            # base case
            if num == 1:
                return 1
            if num == 2:
                return 2
            
            # the actual recursive part, then assign to the hash set
            res = rec(num - 1) + rec(num - 2)

            hash_set[num] = res
            return res
        
        return rec(n)

