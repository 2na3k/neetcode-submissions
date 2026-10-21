class MyHashSet:
    def __init__(self):
        self.data = []

    def add(self, key: int) -> None:
        if key not in self.data:
            self.data.append(key)

    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.data


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


# okay now imma do the linkedlist

# class ListNode:
#     def __init__(self, key: int):
#         self.key = key
#         self.next = None

# class MyHashSet:
#     def __init__(self):
#         self.set = [ListNode(0) for _ in range(10**4)]  # got the bound, now you're learning that thing
        
    
#     def add(self, key: int):
#         cur = self.set[key % len(self.set)]
#         while cur.next:
#             if cur.next.key == key:
#                 return
#             cur = cur.next
#         cur.next = ListNode(key)

#     def remove(self, key: int) -> None:
#         cur = self.set[key % len(self.set)]
#         while cur.next:
#             if cur.next.key == key:
#                 cur.next = cur.next.next    # 1 -> 2 - >3 then turn to 1->3, skip 2
#                 return
#             cur = cur.next
        
#     def contains(self, key: int):
#         cur = self.set[key % len(self.set)]
#         while cur.next:
#             if cur.next.key == key:
#                 return True
#         return False


class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for _ in range(10**4)]

    def add(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False



