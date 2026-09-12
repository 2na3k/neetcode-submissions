# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         """
#         Not the solution since this did not handle the duplication for those things
#         """
#         res = []

#         candidates.sort()

#         def dfs(i, cur, total):
#             if total == target:
#                 res.append(cur.copy())
#                 return None
            

#             if total > target or i == len(candidates):
#                 return None

#             cur.append(candidates[i])
#             dfs(i + 1, cur, total + candidates[i])
#             cur.pop()
#             dfs(i + 1, cur, total)

#         dfs(0, [], 0)
#         return res

class Solution:
    def combinationSum2(self, candidates, target):
        res = set()
        candidates.sort()

        def generate_subsets(i, cur, total):
            # technically breaking condition
            if total == target:
                res.add(tuple(cur))
                return
            if total > target or i == len(candidates):  # no valid combination or the pointer point to the end of the thing
                return

            # 2 cases: include candidates[i] and not include that

            # include the candidate
            cur.append(candidates[i])
            generate_subsets(i + 1, cur, total + candidates[i])

            # not include
            cur.pop()

            # moving the pointer [1,1,1,2,3] then the pointer should be at 2
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1 # moving that pointer
            generate_subsets(i + 1, cur, total)

        generate_subsets(0, [], 0)
        return [list(combination) for combination in res]