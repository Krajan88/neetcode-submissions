# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_node = head
        last_node = None


        while cur_node is not None:
            next_node = cur_node.next
            cur_node.next = last_node
            last_node = cur_node
            cur_node = next_node

        return last_node