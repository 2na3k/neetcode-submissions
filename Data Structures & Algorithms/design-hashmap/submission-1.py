class MyHashMap:

    def __init__(self):
        ...

    def put(self, key: int, value: int) -> None:
        ...

    def get(self, key: int) -> int:
        ...

    def remove(self, key: int) -> None:
        ...


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


class MyHashMap:

    def __init__(self):
        self.map = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1

# do i care?
# fine i care, linkedlist implementation


class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    def __init__(self):
        self.map = [ListNode() for _ in range(1000)]
    
    def hash(self, key: int) -> int:
        # back to basic: really simple hash value
        return key % len(self.map)
    
    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hash(key)]
        
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.map[self.hash(key)].next

        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        
        return -1


    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
    










