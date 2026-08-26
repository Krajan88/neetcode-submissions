# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #if None, don't include a value for that
        """
        Alrighty so make a list, append to that and pop things from the left. I guess you could track the length of the list, and thats for how many times you
        have to pop it. So say you have 2 nodes in the list from the starting root. You check the length, its 2!. You pop 2 items and append their left and 
        right (going from left ot right item).

        For a None node, don't add anything to the queue.

        This process repeats until the queue is empty.

        """
        if root is None:
            return []

        res = []

        queue = deque([root])

        while queue:
            layer = []
            size = len(queue)
            

            for i in range(size):
                node = queue.popleft()
                if node is None:
                    continue

                layer.append(node.val)
                
                left, right = node.left, node.right
                
                if left:
                    queue.append(left)

                if right:
                    queue.append(right)

            res.append(layer)
           
        return res