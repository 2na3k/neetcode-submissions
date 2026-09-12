class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_s = 0
        res = 0
        l, r = 0, len(heights) -1 

        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        
        return res