# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
My approach but without using an entire inorder list

1) Keep track of the current index of anode
2) Inorder traversal - update the index once we reached bottom left of each parent, that is the index of the current node.
3) Once self.index == self.k, that means we are currently at the kth smallest node, since we did inorder traversal. So set self.res to that
4) Because we're at the kth smallest node now, we can just keep returning


"""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.index = 0
        self.res = root.val

        def dfs(root):
            if self.index == self.k:
                return
                
            if root is None:
                return

            left, right = root.left, root.right

            dfs(left)
            

            self.index += 1
            if self.index == self.k:
                self.res = root.val
                return

            dfs(right)
         
            return
        
        dfs(root)
        return self.res



