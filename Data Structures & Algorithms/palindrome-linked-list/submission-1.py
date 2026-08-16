# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #use fast and slow pointer to reverse second half of the list 
        #and deploy another slow pointer at the start

        slow, fast = head, head

        #1. find the middle of the list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

    
        #2. reverse the middle
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt


        #3. check weather lists or palindromes
        """
        Why while prev is not None rather than prev.next is not None?
            doing .next would skip checking the last element for an even list

            for an odd list it doesnt matter since at that point head would approach the middle
            and the last node of the reversed one is the middle too so its trivially true
        """
        while prev is not None:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next

        
        return True
        #3. keep traversing and copmaring slow (thats the middle) and slow2 (new deployed slow)
        #until slow is None
        