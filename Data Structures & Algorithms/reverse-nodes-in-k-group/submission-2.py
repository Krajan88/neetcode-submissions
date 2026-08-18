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
            tail = self.findKth(prevTail,k) #tail of the current list

            if tail is None:
                break

            nextGroup = tail.next #head of the next group

            prev = nextGroup #we want the first node from current list to point to next segment's head (new tail point to next's head)
            cur = prevTail.next #the head of our current segment
            
            while cur is not nextGroup:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            
            #here prevTail is now the current tail after reversal and tail is the head
            temp = prevTail.next
            prevTail.next = tail #<---this points the previous segment's tail to now the new head after reversal
            prevTail = temp #Updates head of previous list to head of current list


        return dummy.next
            

    
    def findKth(self, cur, k):
        while cur is not None and k>0:
            cur = cur.next
            k-=1
        return cur