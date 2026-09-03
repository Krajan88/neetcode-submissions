# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = root.val

        def findPath(root):
            if root is None:
                return 0

            leftMax = findPath(root.left)
            rightMax = findPath(root.right)

            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)

            self.maxPath = max(self.maxPath, root.val+leftMax+rightMax)

            return root.val + max(leftMax, rightMax)

        findPath(root)
        
        return self.maxPath