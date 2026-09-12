class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if len(s1) == len(s2):
            return sorted(s1) == sorted(s2)

        ss1 = sorted(s1)
        l, r = 0, len(s1)
        
        while l < len(s2) - len(s1) + 1:
            window = s2[l:r]
            print(f"window={window}")
            if ss1 == sorted(window):
                return True
            l+=1
            r+=1
        return False