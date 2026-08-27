# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        
        def dfs(root, res):
            if root is None:
                return

            l, r = root.left, root.right

            dfs(l, res)
            res.append(root.val)
            dfs(r, res)

            return res

        res = dfs(root,res)
        
        for i in range(len(res)-1):
            if res[i+1] <= res[i]:
                return False

        return True

        
        """
        1. Do inorder traversal of the tree and keep the values in a list
        2. Compare the most recently added added values
            -if at any point the list is not sorted (not increasing), its not a bst
        
        Since for a bst, the numbers using an inorder traversl will always be increasing.

        """
       