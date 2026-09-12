# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

#         # brute force, but goes wrong somehow, fix later
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 print(f"i={i}, j={j}")
#                 if nums[j] == nums[i] and abs(i - j) <= k:
#                     return True
#         return False


# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

#         # brute force, same as my hand written code but failed too, exceed whatever
#         for i in range(len(nums)):
#             for j in range(i+1, min(len(nums), i + k + 1)):
#                 print(f"i={i}, j={j}")
#                 if nums[j] == nums[i]:
#                     return True
#         return False



# do the hashmap solution

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}

        for i in range(len(nums)):
            if nums[i] in mp and i - mp[nums[i]] <= k:
                return True
            mp[nums[i]] = i
        
        return False