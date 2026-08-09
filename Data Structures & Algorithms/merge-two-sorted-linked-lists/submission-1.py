# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #dummy node is just a node to have an easy access to the linked list we want to return.
        #We set tail = dummy so that the first node we connect will be connected to the dummy
        #and any subsequent connections will be to the tail basically
        dummy = ListNode()
        tail = dummy


        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
                
            else: 
                tail.next = list2
                tail = tail.next
                list2 = list2.next

        
        if list1 is None:
            while list2 is not None:
                tail.next = list2
                tail = tail.next
                list2 = list2.next

        if list2 is None:
            while list1 is not None:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
                
        return dummy.next
