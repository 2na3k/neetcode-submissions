class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # using max heap + dijkstra pls
        # idc abotu those stupid people

        # ofc: forming the adj

        adj = defaultdict(list)

        for i in range(len(edges)):
            # 2 ways?
            src, dst = edges[i]
            adj[src].append((dst, succProb[i]))
            adj[dst].append((src, succProb[i]))
        

        # max heap
        pq = [(-1, start_node)]
        visit = set()


        while pq:
            prob, cur = heapq.heappop(pq)
            visit.add(cur)

            if cur == end_node:
                return -prob

            for neigh, eprob in adj[cur]:
                if neigh not in visit:
                    heapq.heappush(pq, (prob * eprob,  neigh))


        return 0.0