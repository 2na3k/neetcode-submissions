# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next: Optional[ListNode] = None):
#         self.val = val
#         self.next = next

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         node = ListNode()

#         # if list1 is None:
#         #     return list2
#         # if list2 is None:
#         #     return list1
        
#         while list1 and list2:
#             if list1.val < list2.val:
#                 node.next = list1
#                 list1 = list1.next
#             else:
#                 node.next = list2
#                 list2 = list2.next
        
#             node = node.next

#         return node.next
        
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val:
                node.next=list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
            print(f"node: {node.val}, node next {node.next}")
        
        if list1:
            node.next = list1
        else:
            node.next = list2
        
        return dummy.next