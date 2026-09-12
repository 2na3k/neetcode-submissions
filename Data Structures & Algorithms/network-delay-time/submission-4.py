class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # graph construction
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        dist = {node: float('inf') for node in range(1, n+1)}

        def dfs(node, time):
            if time >= dist[node]:
                return
            
            dist[node] = time
            for neigh, w in adj[node]:
                dfs(neigh, time + w)
            
        dfs(k, 0)
        res = max(dist.values())
        return res if res < float('inf') else -1



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

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # try to flatten the things down
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        dist = {node: float('inf') for node in range(1, n+1)}
        dist[k] = 0

        # still keep pq as list(set(dist, node))
        pq = [(0, k)]

        while pq:
            dst, node = heapq.heappop(pq)
            if dist[node] < dst:
                continue
            for adj_node, wt in adj[node]:
                if dst + wt < dist[adj_node]:
                    dist[adj_node] = dst + wt
                    heapq.heappush(pq, (dist[adj_node], adj_node))
        
        ans = max(dist.values())
        return ans if ans < float('inf') else -1

class Solution:
    # shortest path????
    def networkDelayTime(self, times, n, k):
        # idk why they called that shortest path

        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        dist = {node: float('inf') for node in range(1, n+1)}
        dist[k] = 0

        # differences: put this as a heap then put this to a deque
        q = deque([(k, 0)]) # just like the old days

        while q:
            node, time = q.popleft()    # act like a minimum storage

            if dist[node] < time:
                continue
            
            for nei, w in adj[node]:
                if time + w < dist[nei]:
                    dist[nei] = time + w
                    q.append((nei, time + w))
        
        res = max(dist.values())
        return res if res < float('inf') else -1
        
