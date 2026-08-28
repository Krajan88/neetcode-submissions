# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.k = k
        self.res = root.val


        def dfs(root):
            if root is None:
                return

            left, right = root.left, root.right

            dfs(left)
            self.count += 1
            if self.count == self.k:
                self.res = root.val
            dfs(right)

            return

        dfs(root)
        return self.res
        