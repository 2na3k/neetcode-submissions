class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)

        for s, d, w in edges:
            adj[s].append((d, w))

        
        dist = {}

        hq = [(0, src)] # setup the source first

        while hq:
            w1, n1 = heapq.heappop(hq)
            if n1 in dist:
                continue    # = vistied then skip
            dist[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in dist:
                    heapq.heappush(hq, (w1 + w2, n2))
            
        # fill the missing node
        for i in range(n):
            if i not in dist:
                dist[i] = -1
        
        return dist
