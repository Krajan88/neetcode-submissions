# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def dfs(root):
            if root is None:
                return 0
            nonlocal max_depth

            left = dfs(root.left)
            right = dfs(root.right)
            height = 1 + max(left,right)

            max_depth = max(height, max_depth)

            return height

        dfs(root)
        return max_depth