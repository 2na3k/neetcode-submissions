# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         stack = []
#         for a in asteroids:
#             if len(stack) == 0:
#                 print("stack len = 0 case")
#                 stack.append(a)
            
#             # moving up to the main check
#             else:
#                 if stack[-1] * a > 0:
#                     # same way
#                     print("running in the same place")
#                     stack.append(a)
#                 else:
#                     # collision handling
#                     last = stack[-1]
#                     stack.pop()
                    
#                     # explosion handling
#                     if abs(a) > abs(last):
#                         print("a > last one")                 
#                         stack.append(a)
#                     elif abs(a) < abs(last):
#                         print("a < last one")
#                         stack.append(last)
#                     else: # same abs
#                         print("same thing, no append just blow up!!!")
#         return stack

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            print(f"iteration to {a}")
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                print(f"a={a}, last={stack[-1]}, diff={diff}")
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a:
                "this is which case again?"
                stack.append(a)
        return stack