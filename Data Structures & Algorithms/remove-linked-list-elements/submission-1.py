# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        cur = dummyNode
        
        while cur is not None and cur.next is not None:
            #needed a while here in the case the next node after the one we need to remove also has 
            #the target value
            while cur.next is not None and cur.next.val == val:
                cur.next = cur.next.next

            cur = cur.next

        return dummyNode.next