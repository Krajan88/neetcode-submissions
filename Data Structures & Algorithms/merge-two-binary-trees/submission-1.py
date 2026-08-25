# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2

        if root2 is None:
            return root1

        sol = root1

        self.merge(root1,root2)

        return sol



    def merge(self, root1,root2):
        if root1 is None or root2 is None:
            return 
        
        if root1 != root2:
            root1.val += root2.val

        if root1.left is None:
            root1.left = root2.left

        if root1.right is None:
            root1.right = root2.right

        

        self.merge(root1.left, root2.left)
        self.merge(root1.right,root2.right)
    

