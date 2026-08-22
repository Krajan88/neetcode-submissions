# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        list1, list2 = [], []

        def dsf(root, vals):
            if not root:
                vals.append(None)
                return 


            left = dsf(root.left, vals)
            right = dsf(root.right, vals)

            vals.append(root.val)

            return vals

        
        list1 = dsf(p, list1)
        list2 = dsf(q, list2)

        print(list1)
        print(list2)

        return list1 == list2

