# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
What do we need to keep track of inside of the recursion:

1) The root we're at (indexed 1, strating from bottom left node)
2) How many times the recursion happened


"""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.index = 0
        self.res = root.val

        def dfs(root):
            if root is None:
                return

            left, right = root.left, root.right

            dfs(left)
            if self.index == self.k:
                return

            self.index += 1
            if self.index == self.k:
                self.res = root.val
                return

            dfs(right)
         
            return
        
        dfs(root)
        return self.res



