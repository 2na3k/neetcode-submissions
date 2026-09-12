class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            
            # Check if the left half is normally sorted
            if nums[l] <= nums[m]:
                # Is the target within this sorted left half?
                if nums[l] <= target < nums[m]:
                    r = m - 1  # Look left
                else:
                    l = m + 1  # Look right
            # Otherwise, the right half must be normally sorted
            else:
                # Is the target within this sorted right half?
                if nums[m] < target <= nums[r]:
                    l = m + 1  # Look right
                else:
                    r = m - 1  # Look left
                    
        return -1

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         # Create pairs of (number, original_index) and sort them
#         indexed_nums = [(num, i) for i, num in enumerate(nums)]
#         indexed_nums.sort() # Sorting is kept at the top!

#         # TIL: sort 
        
#         l, r = 0, len(indexed_nums) - 1
        
#         # Binary search on the sorted pairs
#         while l <= r:
#             m = l + (r - l) // 2
#             val, original_index = indexed_nums[m]
            
#             if val == target:
#                 return original_index # Return the original index we saved
#             elif val < target:
#                 l = m + 1 # Target is larger, search the right half
#             else:
#                 r = m - 1 # Target is smaller, search the left half
                
#         return -1
