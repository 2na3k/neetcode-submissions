class Solution:
    ### the palindome one
    def isValid(self, s: str) -> bool:
        #     pat_m = {
        #         "[": "]",
        #         "{": "}",
        #         "(": ")"
        #     }



        #     # of course, false
        #     if len(s) % 2 != 0:
        #         return False

        #     half = int(len(s) / 2)
        #     for i in range(half):
        #         print(s[i])
        #         print(s[-(i+1)])
        #         print()
        #         if s[-(i+1)] != pat_m.get(s[i]):
        #             return False
        
        #     return True

        # closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        
        # stack = []
        # for c in s:
        #     if c in closeToOpen:
        #         if stack and stack[-1] == closeToOpen[c]:
        #             stack.pop()
        #         else:
        #             return False
        #     else: stack.append(c)
            

        # return True if len(stack) == 0 else False

        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        stack = []
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] ==  closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else: stack.append(c)
        return True if len(stack) == 0 else False

    