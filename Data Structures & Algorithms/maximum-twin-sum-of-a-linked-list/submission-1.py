# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #1. find middle using slow and fast pointers
        #2. reverse the 2nd half
        #3. deploy two slow pointers and find the biggest sum

        slow = head
        fast = head

        while fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next


        prev = None
        cur = slow.next #head of the 2nd half that we wanna reverse

        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        slow1 = head
        slow2 = prev

        twinSum, maxSum = 0, 0

        while slow1.next is not None:
 
            twinSum = slow1.val + slow2.val
            if twinSum > maxSum:
                maxSum = twinSum

            slow1 = slow1.next
            slow2 = slow2.next

        return maxSum