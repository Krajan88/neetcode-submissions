# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None: #null is always a subtree of a non-empty / empty tree (look at the children)
            return True

        if root is None:
            return False

        if self.sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)



    def sameTree(self, root, subRoot):
        if root is None and subRoot is None:
            return True

        if root is None or subRoot is None:
            return False

        if root.val != subRoot.val:
            return False

        return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)