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

        heapq.heappush(pq,(0, src, 0))

        while pq:
            step, node, cost = heapq.heappop(pq)
            if step <= k and node in adj_list:
                for nextNode, weight in adj_list[node]:
                    if weight + cost < nodeMap[nextNode]:
                        nodeMap[nextNode] = weight + cost
                        heapq.heappush(pq,(step+1, nextNode, weight+cost))

        
        return nodeMap[dst] if nodeMap[dst] != float('inf') else -1