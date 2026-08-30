# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = root.val

        def dfs(root):
            if root is None:
                return 0

            nonlocal maxPath

            maxLeft = dfs(root.left)
            maxRight = dfs(root.right)

            maxLeft = max(maxLeft, 0)
            maxRight = max(maxRight, 0)

            maxPath = max(maxPath, maxLeft+maxRight+root.val)

            return root.val + max(maxLeft, maxRight)

        dfs(root)
        return maxPath


        