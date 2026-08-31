# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        str1 = ""
        str2 = ""
        

        def dfs1(root):
            nonlocal str1
            if root is None:
                str1 += "n"
                return

            str1 += str(root.val)

            dfs1(root.left)
            dfs1(root.right)

            return

        def dfs2(root):
            nonlocal str2
            if root is None:
                str2 += "n"
                return

            str2 += str(root.val)

            dfs2(root.left)
            dfs2(root.right)
            return

        dfs1(root)
        dfs2(subRoot)

        print(str1)
        print(str2)

        return str2 in str1