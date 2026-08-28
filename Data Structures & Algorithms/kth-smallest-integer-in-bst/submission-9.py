class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.index = 0
        self.res = root.val

        def dfs(root):
            if root is None:
                return False

            if dfs(root.left):
                return True

            self.index += 1

            if self.index == k:
                self.res = root.val
                return True

            if dfs(root.right):
                return True

            return False

        dfs(root)
        return self.res