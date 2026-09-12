class Solution:
    def validPalindrome(self, s: str) -> bool:
        for idx, c in enumerate(s):
            # remove the char
            new_s = s[:idx] + s[idx+1:]
            print(new_s)
            new_sl = [c for c in new_s]
            rsl = new_sl[::-1]
            if new_s == "".join(rsl):
                return True
        return False