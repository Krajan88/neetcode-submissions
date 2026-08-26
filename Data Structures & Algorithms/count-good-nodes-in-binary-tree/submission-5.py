# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #everything in the path of a node x to the binary tree's root cannot have a node of value greater than itself
        """
        The process: track the greatest value parent encountered so far. If cur node >=, increment the 
        number of good nodes AND update the greatest value parent encountered so far.

        dfs(root,gvp) // gvp - greatest value parent
        if root.val >= gvp:
            gvp = root.val
            self.goodNoeds +=1

        """


        self.goodNodes = 0

        def dfs(root,gvp):
            if root is None:
                return

            if root.val >= gvp:
                self.goodNodes +=1
                gvp = root.val

            left, right = root.left, root.right


            dfs(left, gvp)
            dfs(right, gvp)

        dfs(root, root.val)

        return self.goodNodes
        