# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Using slow and fast pointer to actually doing all of this
        
        3 steps:
        1. Getting the midpoint (first half and second half of the thing)
        2. Reverse the second half of the thing
        3. Merge both of them together
        """

        # first stage: dealing with the thing
        first: ListNode = head
        second = head.next
        
        while second and second.next:
            first = first.next
            second = second.next.next
        second = first.next
        
        # second stage: reverse the second half
        
        prev = first.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # third one, merge all the things
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
            
            