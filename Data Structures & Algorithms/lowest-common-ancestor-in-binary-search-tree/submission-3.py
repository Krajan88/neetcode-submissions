# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Brute force solution: you're traversing the whole tree. Instead, you can compare the value of the node you're currently at to p and q 

    """
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

            if root.val >= self.smallVal and root.val >= self.bigVal:
                dsf(left)
            if root.val <= self.smallVal and root.val <= self.bigVal:
                dsf(right)
        
        dsf(root)

        return self.sol