# class Solution:
#     def numRescueBoats(self, people: List[int], limit: int) -> int:
#         people.sort()

#         sorted_p = people[::-1]  # Heaviest to lightest
#         n = len(sorted_p)

#         count = 0
#         l = 0
#         used = [False] * n

#         # Brute force
#         while l < n:
#             # Skip people who were already paired
#             if used[l]:
#                 l += 1
#                 continue

#             # The current person needs a boat, even if they ride alone
#             count += 1
#             used[l] = True

#             # Search from the lightest person toward the current person
#             for i in range(n - 1, l, -1):
#                 if not used[i] and sorted_p[l] + sorted_p[i] <= limit:
#                     used[i] = True
#                     break

#             l += 1

#         return count


# from typing import List

# class Solution:
#     def numRescueBoats(self, people: List[int], limit: int) -> int:
#         people.sort(reverse=True)

#         count = 0

#         # Brute force
#         while people:
#             heaviest = people.pop(0)
#             count += 1  # The heaviest person needs a boat either way

#             # Search from the lightest person backward
#             for i in range(len(people) - 1, -1, -1):
#                 if heaviest + people[i] <= limit:
#                     people.pop(i)
#                     break

#         return count


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res, l, r = 0, 0, len(people) - 1
        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remain >= people[l]:
                l += 1
        return res