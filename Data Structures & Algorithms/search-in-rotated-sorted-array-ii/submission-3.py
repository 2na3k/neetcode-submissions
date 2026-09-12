# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         d = list(set(nums))
#         sorted(d)
#         print(d)
#         l, r = 0, len(d) - 1
        
#         while l <= r:
#             m = l + (r - l) // 2
#             if d[m] == target:
#                 return True
#             elif d[m] < target:
#                 l = m + 1
#             else:
#                 r = m - 1
                    
#         return False


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return True
            
            # Check if the left half is normally sorted
            if nums[l] < nums[m]:
                # Is the target within this sorted left half?
                if nums[l] <= target < nums[m]:
                    r = m - 1  # Look left
                else:
                    l = m + 1  # Look right
            # Otherwise, the right half must be normally sorted
            elif nums[l] > nums[m]:
                # Is the target within this sorted right half?
                if nums[m] < target <= nums[r]:
                    l = m + 1  # Look right
                else:
                    r = m - 1  # Look left
            else:
                l += 1
                    
        return False