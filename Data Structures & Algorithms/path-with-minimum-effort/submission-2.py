class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        minHeap = [[0,0,0]] # diff, row, col
        visit = set()

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)
            if (r, c) in visit:
                continue
        

            visit.add((r, c))

            if (r, c) == (rows -1, cols -1):
                return diff
            
            for dr, dc in directions:
                newr, newc = r + dr, c + dc

                if (
                    newr < 0 or newc < 0
                    or newr >= rows or newc >= cols
                    or (newr, newc) in visit
                ):
                    continue
                
                new_diff = max(diff, abs(heights[r][c] - heights[newr][newc]))
                heapq.heappush(minHeap, [new_diff, newr, newc])

        return 0

        