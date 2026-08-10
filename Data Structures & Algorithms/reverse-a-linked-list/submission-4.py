# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev
"""
Explanation:
nxt = curr.next:
    Nxt now holds the address of the node that curr was originally pointing to. We need this so that we can go
    through the linked list one by one. After updating what curr points to, we can 'move to the right' of curr node
    and continue the loop

Curr.next meaning:
    Points to the address of the node that is next to curr. By ex. setting curr.next = prev, the node that
    comes NEXT after curr will be prev.

1) prev = curr
2) curr = nxt
    1) Variable prev now refers to the variable curr. Does not change the pointer.
    2) Variable curr now refers to the variable nxt. Does not change the pointer




"""



