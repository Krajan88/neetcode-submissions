# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #the efficient solution does create a new linke dlists with nodes that are sums.
        #this makes it wayyy easier to complete this problem lol

        dummyNode = ListNode(0)
        cur = ListNode(0)
        dummyNode.next = cur
        carry, v1, v2 = 0, 0, 0

        while l1 is not None or l2 is not None or carry != 0:
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0
         

            num = v1+v2+carry

            if num >= 10:
                carry = 1
                num = num % 10
            else:
                carry = 0

            cur.next = ListNode(num)

            #case for when both lists ran out but there is a carry / longer length number than both
            if l1 is None and l2 is None and carry != 0:
                cur.next = ListNode(carry)

            
            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next
            cur = cur.next

        return dummyNode.next.next






