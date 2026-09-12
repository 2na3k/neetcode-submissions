# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         speed = 1
#         while True:
#             tt = 0
#             for pile in piles:
#                 tt += math.ceil(pile/speed)

#             if tt <= h:
#                 return speed
            
#             speed += 1
#         return speed


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        res = r

        while l <= r:
            k = (l+r) // 2
            tt = 0
            for p in piles:
                tt += math.ceil(float(p) / k)

            if tt <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        
        return res