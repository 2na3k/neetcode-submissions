class Solution:
    def reorganizeString(self, s: str) -> str:
        # solve this with heap, of course target time would be onlogn
        
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]

        prev = None
        res = ""

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            cnt, char = heapq.heappop(maxHeap)

            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if cnt != 0:
                prev = [cnt, char]

        return res