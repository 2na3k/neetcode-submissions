class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i, cur):
            if len(cur) == len(digits):
                res.append(cur)
                return
            
            for c in mapping[digits[i]]:
                dfs(i + 1, cur + c)
        
        if digits:
            dfs(0, "")
        return res


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

            
        res = [""]

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        for digit in digits:
            tmp = []
            for cur in res:
                for c in mapping[digit]:
                    tmp.append(cur + c)
            
            res = tmp
        return res

