class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_t = s.split(" ")
        
        s_t_clean = [t for t in s_t if t != '']
        return len(s_t_clean[-1])


# okay let's do that in a more serious manner

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # iteration:
        length = i = 0

        while i < len(s):
            if s[i] == ' ':
                while i < len(s) and s[i] == ' ':
                    i += 1
                if i == len(s):
                    return length
                length = 0
            else:
                length += 1
                i += 1
        
        return length