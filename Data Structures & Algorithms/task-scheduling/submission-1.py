class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # construct the max heap
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        # cycle: one loop will add all of the distinct chars in the tasks
        # nah fuck it since each time you done the time -> should be another thing

        time = 0

        q = deque()

        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]

            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt: # like it is the time for the task
                    q.append([cnt, time + n])   # AGAIN, we're using negative amount of count -> plus to minus
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time