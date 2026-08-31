# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.nums = []
        res = 0

        def dfs(root, path):
            if root is None:
                return

            path = path*10 + root.val

            left, right = root.left, root.right

            if left is None and right is None:
                self.nums.append(path)


            dfs(left, path)
            dfs(right, path)

            return

        dfs(root, 0)
        
        for num in self.nums:
            res += num

        return res