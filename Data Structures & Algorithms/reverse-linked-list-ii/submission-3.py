# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevTail = dummy

        for i in range(left-1):
            prevTail = prevTail.next
        
        
        segmentHead = prevTail.next #will be at the end after reversal
        start = prevTail.next
        tail = start
        cur = start
        prev = prevTail
        
        for i in range(right-left):
            tail=tail.next
        
        nextHead = tail.next


        while cur is not nextHead:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur=nxt
    

        prevTail.next = prev
        segmentHead.next = cur
        return dummy.next

        
            

        