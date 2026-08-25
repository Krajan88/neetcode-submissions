# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        #find sum of all numbers that are [x,y] inclusive. So if tree has 1 2 3 4 5 6 7 and x = 2 y =6, add 2 3 4 5 6.
        if root is None:
            return 0
        
        self.l = low
        self.h = high
        num = 0

        def dsf(root, num):
            if root is None:
                return num

            print(num)
            
            if root.val >= self.l and root.val <= self.h:
                num += root.val

            left, right = root.left, root.right

            num = dsf(left, num)
            num = dsf(right, num)

            return num

        return dsf(root, num)

