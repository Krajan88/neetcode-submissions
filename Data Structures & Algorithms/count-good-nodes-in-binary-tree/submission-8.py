# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, gvp):
            if node is None:
                return 0
            count = 1 if node.val >= gvp else 0
            gvp = max(gvp, node.val)
            return count + dfs(node.left, gvp) + dfs(node.right, gvp)
        return dfs(root, root.val)