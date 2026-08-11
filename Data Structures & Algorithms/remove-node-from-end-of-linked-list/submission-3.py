# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #slow and fast nodes. they are n nodes apart. Once fast is None, slow.next = target to delete. Set slow.next slow.next.next
        slow, fast = head, head

        for i in range(n):
            fast = fast.next

        while True:
            if fast is None:
                return slow.next
            elif fast.next is None:
                slow.next = slow.next.next
                break

            slow = slow.next
            fast = fast.next
                

        return head




            