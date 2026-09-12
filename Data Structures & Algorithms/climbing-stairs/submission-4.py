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


class Solution:
    def climbStairs(self, n: int) -> int:
        # linear solution
        if n == 1:
            return 1
        if n == 2:
            return 2
        # cache = [None] * n # not sure
        cache = [1, 2]  # will grow linear

        # cache[1] = 1
        # cache[2]

        out = 0

        for i in range(2, n):   # you need the n index
            print(f"i-2={i-2}")
            print(f"i-1={i-1}")

            cache.append(cache[i - 1] + cache [i - 2])
        
        return cache[-1]
        
        
        
