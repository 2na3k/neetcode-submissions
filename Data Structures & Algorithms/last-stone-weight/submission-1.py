class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            cur = stones.pop() - stones.pop()
            if cur:
                stones.append(cur)
        
        return stones[0] if stones else 0


class Solution:
    # do the heap ones
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap since we need to detect the fucking heap

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second)
        
        stones.append(0)
        return abs(stones[0])

    