class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]

        pc = set()  # placed
        ppos = set()    # diag +
        pneg = set()    # diag -
        out = []


        def backtrack(r):
            # iterate through row -> then iterate through cols
            if r == n:
                # break the recursive
                b = board[:]
                sol = []
                for col in b:
                    sol.append("".join(col[:]))
                out.append(sol)
                return
            else:
                for c in range(n):
                    # base case
                    if c in pc or r + c in ppos or r - c in pneg:
                        continue    # skip for the case
                    
                    board[r][c] = "Q"
                    pc.add(c)
                    ppos.add(r+c)
                    pneg.add(r-c)

                    backtrack(r+1)

                    # actually backtrack
                    board[r][c] = "."
                    pc.remove(c)
                    ppos.remove(r+c)
                    pneg.remove(r-c)

        backtrack(0)
        return out