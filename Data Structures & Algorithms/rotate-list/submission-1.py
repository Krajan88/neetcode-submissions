# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None:
            return None

        cur = head
        size = 1

        

        while cur.next is not None:
            cur = cur.next
            size += 1
        
        k = k%size
        
        cur.next = head

        for i in range(size-k):
            cur = cur.next

   
        newHead = cur.next
        cur.next = None


        return newHead