# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < q.val:
            self.smallVal = p.val
            self.bigVal = q.val
        else:
            self.smallVal = q.val
            self.bigVal = p.val

        self.sol = None

        
        def dsf(root):
            if self.sol is not None:
                return

            if root is None:
                return

            if root.val >= self.smallVal and root.val < self.bigVal or root.val > self.smallVal and root.val <= self.bigVal:
                self.sol = root
                return

            left, right = root.left, root.right

            dsf(left)
            dsf(right)
        
        dsf(root)
        print(self.sol.val)
        return self.sol