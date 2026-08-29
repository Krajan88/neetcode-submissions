# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        self.res = None

        def dfs(root):
            if root is None:
                return 

            print(root.val)

            if self.count == 0:
                return

            dfs(root.left)
           

            self.count -= 1

            if self.count == 0:
                self.res = root
                return

            dfs(root.right)

        dfs(root)
        return self.res.val