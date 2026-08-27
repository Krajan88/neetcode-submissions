# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, left, right): #left and right are the left and right boundaries
            if not node:
                return True #empty bst is still technically a bst

            if not (node.val < right and node.val > left):
                return False

            return valid(node.left, left, node.val) and valid(node.right, node.val, right) #left subtree has to be less than the parent, so update the right boundary (max)
        
        return valid(root, float("-inf"), float("inf"))



"""
BST
-every left child have to be less than the parent
(its children will also have to be less than that parent)

-every right child will have to be greater than the parent
(its children will also have to be greater than that parent)
"""