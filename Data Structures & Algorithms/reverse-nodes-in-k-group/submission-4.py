# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prevTail = dummy

        while True:
            tail = self.findTail(prevTail,k) 

            if tail is None:
                break

            nextHead = tail.next #head of the next segment

            prev = nextHead
            cur = prevTail.next

            while cur is not nextHead:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt


            temp = prevTail.next #saving the reference so that segments are connected: dummy 321, prevTail.next here is 1 not 3
            prevTail.next = tail#now dummy points to the 3, not 1.
            prevTail = temp#now prevTail is 1.
            """
prevTail is reassigned to the node that used to be the head of the just-reversed group, but which has already finished transitioning into that group's tail by the time the assignment happens.


prevTail = head, but since the segment has been reversed, head is the tail.
            """


        return dummy.next


    def findTail(self, cur, k):
        while cur is not None and k > 0:
            cur = cur.next
            k-=1

        return cur