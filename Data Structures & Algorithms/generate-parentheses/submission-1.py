class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # brute force DFS
        res = []
        
        def valid(s):
            open = 0
            for c in s:
                open += 1 if c == '(' else -1
                if open < 0:
                    return False
            return not open
        
        def dfs(s):
            if n * 2 == len(s):
                if valid(s):
                    res.append(s)
                return
            
            dfs(s + '(')
            dfs(s + ')')
        
        dfs("")
        return res


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openn, closen):
            if openn == closen == n:
                res.append("".join(stack))
                return
            
            if openn < n:
                stack.append("(")
                backtrack(openn+1, closen)
                stack.pop()
            if closen < openn:
                stack.append(")")
                backtrack(openn, closen+1)
                stack.pop()
        
        backtrack(0, 0)
        return res
