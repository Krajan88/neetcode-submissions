"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        #dummy node for the start of copied list
        dummyNode = Node(0)
        
        curCopy = dummyNode
        cur = head

        old_to_new = {}


        #hard copy of the .next portion
        while cur is not None:
            curCopy.next = Node(cur.val)
            
            old_to_new[cur] = curCopy.next

            cur = cur.next
            curCopy = curCopy.next


        curCopy = dummyNode.next
        cur = head

        while cur is not None:
            if cur.random is None:
                curCopy.random = None
            else:
                curCopy.random = old_to_new[cur.random]

            cur = cur.next
            curCopy = curCopy.next

        return dummyNode.next

        

        