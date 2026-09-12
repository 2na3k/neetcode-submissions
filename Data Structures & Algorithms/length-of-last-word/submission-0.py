class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_t = s.split(" ")
        
        s_t_clean = [t for t in s_t if t != '']
        return len(s_t_clean[-1])