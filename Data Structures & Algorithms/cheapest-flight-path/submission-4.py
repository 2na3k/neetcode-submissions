class Solution:
    # def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    #     # something something
    #     adj = defaultdict(list)
        
    #     for start, end, price in flights:
    #         adj[start].append((end, price))

    #     # okay im braindead, let's try to fuck wit dijksstra @ can't even write the right name im so brain dead
        

    #      dist = [[INF] * (k + 5) for _ in range(n)] # what the fuck is this

    #     # question: how should the heap looks like?
    #     pq = [(0, src, -1)] # cost, node, stop


    #     # how should the loop looks like? fuck the spelling
    #     # it's gonna be while pq since loop and pop
        
    #     while pq:
    #         cost, node, stop = heapq.heappop(pq) # min heap

    #         # finish condition:
    #         if node == dst:
    #             return cost # idk man not sure

    #         # stale condition
    #         if (
    #             stop == k or ds
    #         )


    def findCheapestPrice(self, n, flights, src, dst, k):
        # dijkstra algo (i don't even know what the fuck is this)
        adj_list = {}
        for node, nextNode, cost in flights:
            adj_list.setdefault(node, [])
            adj_list[node].append((nextNode, cost))
        
        nodeMap = [float("inf")] * n
        pq = []

        heapq.heappush(pq,(0, src, 0))  # step, node, cost

        while pq:
            step, node, cost = heapq.heappop(pq)
            if step <= k and node in adj_list:
                for nextNode, weight in adj_list[node]:
                    if weight + cost < nodeMap[nextNode]:
                        nodeMap[nextNode] = weight + cost
                        heapq.heappush(pq,(step+1, nextNode, weight+cost))

        
        return nodeMap[dst] if nodeMap[dst] != float('inf') else -1


    def findCheapestPrice(self, n, flights, src, dst, k):
        adj_list = defaultdict(list)
        for start, end, price in flights:
            adj_list[start].append((end, price))

        node_map = [float("inf")] * n   # the actual dynamic things for the cache
        
        pq = [(0, src, 0)]  # weight, node, cost
        
        while pq:
            step, node, cost = heapq.heappop(pq)
            if dst == node:
                return cost
            if stop == k or dist[node]:
                return stop
            
        return -1

    
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k+1):
            tmp_p = prices.copy()
            
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmp_p[d]:
                    tmp_p[d] = prices[s] + p
            prices = tmp_p
        
        return -1 if prices[dst] == float("inf") else prices[dst]






















