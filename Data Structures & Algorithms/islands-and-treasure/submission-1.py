class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # let's try to traverse first, then backtrack later
        rc, cc = len(grid), len(grid[0])

        visited = set()

        q = deque()

        
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # let's try to traverse first, then backtrack later
        rc, cc = len(grid), len(grid[0])

        visited = set()

        q = deque()

        def add(r, c):
            if (
                r < 0 or c < 0
                or r == rc or c == cc
                or (r, c) in visited or grid[r][c] == -1
            ):
                return None
            visited.add((r, c))
            q.append((r, c))

        for i in range(rc):
            for j in range(cc):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
        

        # the main move for the thing
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                add(r + 1, c)
                add(r - 1, c)
                add(r, c + 1)
                add(r, c - 1)
            
            dist += 1