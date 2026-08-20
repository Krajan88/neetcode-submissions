# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur is not None and cur.next is not None:
            temp = cur.next
            cur.next = ListNode(math.gcd(cur.val, cur.next.val), temp)
            cur = temp
            

        return head

            
