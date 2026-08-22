# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(root):
            if root is None:
                return 0


            left = height(root.left)
            right = height(root.right)

            if abs(right-left)>1:
                right = float('inf')

            return 1 + max(left, right)

        top = height(root)

        if top == float('inf'):
            return False
        else:
            return True