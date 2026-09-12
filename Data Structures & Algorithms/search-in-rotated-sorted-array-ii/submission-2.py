class Solution:
    def search(self, nums: List[int], target: int) -> int:
        d = list(set(nums))
        sorted(d)
        print(d)
        l, r = 0, len(d) - 1
        
        while l <= r:
            m = l + (r - l) // 2
            if d[m] == target:
                return True
            elif d[m] < target:
                l = m + 1
            else:
                r = m - 1
                    
        return False