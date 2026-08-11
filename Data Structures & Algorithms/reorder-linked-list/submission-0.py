# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #use fast and slow pointers to find the middle of the list, reverse the right half
        #and just connect them one by one
        slow, fast = head, head
        
        #use an and rather than an or to see if the second condition is True. If first one is true then it has to check whether the second is true
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next


       #no need for even and off length I don't think
        
        r = slow.next
        slow.next = None
        l = head



        #reversing right side
        prev = None
        cur = r

        #issue: thought 'cur' was the first element of the reversed list.
        #fix: prev is actually the first element. (since the link reversed, recall reverse linked list problem)
        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        l, r = head, prev
        
        #connecting left and right partitions
        while r is not None:
            l_nxt = l.next
            r_nxt = r.next
            
            l.next = r
            r.next = l_nxt
            l = l_nxt
            r = r_nxt



        
"""
Odd length: last value will be regular / forward node
-if fast.next is None, then the slow pointer is located at the middle.
-until we reach the middle, connect the nodes to have the nodes that are advancing like in the original list
-after that, make a reversed linked list 
-connected the two until both .next have a None at the end

Even length: last value will be a reversed node


Do separate checks: if fast is None will work for even length lists and if fast.next is None will work for odd length lists

    #find half of an even list
    if fast is None:

    
    #finds half of an odd list
    elif fast.next is None:


"""