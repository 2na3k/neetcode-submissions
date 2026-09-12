# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get count, since linked list need traversal to see where it goes
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        remove_index = count - n
        
        if remove_index == 0:
            return head.next

        print(f"remove index {remove_index}")
        
        # now, loop til getting shit
        curr = head     # MUST SET THIS AGAIN
        for i in range(0, count-1):
            if i + 1 == remove_index and curr:
                curr.next = curr.next.next
                break
            curr = curr.next
                
        return head
            