# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #use slow and fast pointers to find the middle
        slow, fast = head, head
        
        #use 'and' for conditional not an 'or'. If pointer lands at the last element then the second part of the 'and' will be checked and terminate the loop.
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        #splitting the list into two halves
        r = slow.next
        slow.next = None
        l = head

        #reversing right side
        prev = None
        cur = r

        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        #**remember that after reversing, the first node is prev not cur**

        #setting the first nodes for the two halves
        l, r = head, prev
        
        #connecting the two halves
        while r is not None:
            l_nxt = l.next
            r_nxt = r.next
            
            l.next = r
            r.next = l_nxt
            #forgot to put the l = l_nxt originally
            l = l_nxt
            r = r_nxt



        

"""
The problem breaks down into 3 parts:
1) Find the middle of the linked list and split it into two lists
2) Reverse the second half
3) Connect the nodes from first and second half interchangably
   (l1 -> r1 -> l2 -> r2 -> l3 -> r3...)
"""