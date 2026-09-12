class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # n directed node, k is the node send the signal from
        # graph construction
        graph = [[] for _ in range(n+1)]  # {u: (v, t)}

        for u, v, t in times:
            graph[u].append((v, t))

        # create the loop
        dist = [float('inf')] * (n+1)
        dist[k] = 0 # dist = 0

        # priority queue
        pq = [(0, k)]   # [(distance, node_name)]

        while pq:
            dst, node = heapq.heappop(pq)   # technically get the min heap here, max heap got the -h...
            if dst > dist[node]:
                continue    # due to the shit is weird, break that
            
            for adj_node, wt in graph[node]:
                if dst + wt < dist[adj_node]:
                    dist[adj_node] = dst + wt
                    heapq.heappush(pq, (dist[adj_node], adj_node))
        
        ans = 0

        for i in range(1, n+1):
            if dist[i] == float('inf'):
                return -1
            ans = max(ans, dist[i])

        return ans