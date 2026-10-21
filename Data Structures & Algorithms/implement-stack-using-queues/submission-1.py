class MyStack:
    # yeah i will use only 1 queue fuck them
    # wow this is weird
    # yeah
    def __init__(self):
        self.pq = deque()

    def push(self, x: int) -> None:
        self.pq.append(x)
        for _ in range(len(self.pq) - 1):
            self.pq.append(self.pq.popleft())

    def pop(self) -> int:
        return self.pq.popleft()

    def top(self) -> int:
        return self.pq[0]
        

    def empty(self) -> bool:
        return len(self.pq) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()
    
    def top(self) -> int:
        return self.q1[0]
    
    def empty(self) -> bool:
        return len(self.q1) == 0