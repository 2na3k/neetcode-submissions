# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         # brute force:
#         # i, j = 0, 0
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j] == target:
#                     return True
        
#         return False



# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         """
#         Binary search in the weirdest sense

#         OOM or whatever
#         """
        
#         i = 0
        
#         while i < len(matrix):
#             if target > matrix[i][-1]:
#                 i+=1
#             elif target < matrix[i][-1]:
#                 j = 0
#                 while j < len(matrix[0]):
#                     """technically I could do a mini binary search here but fuck it"""
#                     if matrix[i][j] == target:
#                         return True
#                     else:
#                         j+=1
#             else:
#                 return True
        
#         return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # binary in the cols 
        r, c = 0, n - 1


        while r < m and c >= 0:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True
        return False