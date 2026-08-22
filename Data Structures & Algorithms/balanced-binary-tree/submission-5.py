# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def dfs(root):
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            if abs(right-left) > 1:
                self.balanced = False

            return 1 + max(right,left)
        
        dfs(root)
        return self.balanced
            