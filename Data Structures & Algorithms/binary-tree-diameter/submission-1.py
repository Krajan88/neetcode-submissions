# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest_diameter = 0

        def dfs(root):
            nonlocal largest_diameter
            
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            diameter = left + right

            largest_diameter = max(diameter, largest_diameter)

            return 1+max(left,right)

        dfs(root)
        return largest_diameter