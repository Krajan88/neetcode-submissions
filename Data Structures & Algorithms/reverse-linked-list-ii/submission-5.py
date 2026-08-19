# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prevTail = dummy#tail of the previous, unreversed segment


        for i in range(left-1):
            prevTail = prevTail.next


        curHead=prevTail.next
        curTail = curHead


        for i in range(right-left):
            curTail = curTail.next #tail of the segment we are reversing

        
        nextHead = curTail.next #head of the next segment that comes after the reversed one

        prev = prevTail
        cur = prevTail.next

        curHead = cur
        
        while cur is not nextHead:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        #forgot about changing the pointers for prevTail and curTail...

        prevTail.next = curTail
        curHead.next = nextHead
        
              

        return dummy.next


