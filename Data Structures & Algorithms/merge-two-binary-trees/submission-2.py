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


        def merging(root1, root2): #root1 is the final tree
            if root1 is None or root2 is None:
                return

            if root1 is not root2: #prevents double addition for the case where we changed the root1's child to root2's child since it was empty
                root1.val += root2.val

            if root1.left is None:
                root1.left = root2.left

            if root1.right is None:
                root1.right = root2.right


            merging(root1.left, root2.left)
            merging(root1.right,root2.right)

        merging(root1, root2)

        return root1