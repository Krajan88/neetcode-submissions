# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.sol = False
        self.t = targetSum

        def dsf(root, num): #num = sum of current path
            if root is None:
                return None, num

            num += root.val


            left = root.left
            right = root.right


            if left is None and right is None and num == self.t:
                self.sol = True

            dsf(left, num)
            dsf(right, num)

            num -= root.val


        dsf(root, 0)

        return self.sol




