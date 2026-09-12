# class Solution:
# ? why
#     def removeElement(self, nums: List[int], val: int) -> int:
#         count = 0
#         for i in nums:
#             if i != val:
#                 count += 1
#                 nums[count] = i        
#         return count

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         """The fuck the solution is in the list but why no?"""
#         k = 0
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[k] = nums[i]
        
#         return k

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """WHY THIS LITTLE SHIT WORKS?"""
        tmp = []
        for num in nums:
            if num == val:
                continue
            tmp.append(num)
        for i in range(len(tmp)):
            nums[i] = tmp[i]
        return len(tmp)