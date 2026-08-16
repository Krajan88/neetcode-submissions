# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        array = []
        
        while head is not None:
            array.append(head.val)
            head = head.next
            
        size = len(array)
        
        
        for i in range(math.ceil(size/2)):
            print(size)
            if array[i] != array[size-i-1]:
                return False
                

        return True
