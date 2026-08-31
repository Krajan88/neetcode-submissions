# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            #If root is None, either a) we are at a leaf or b) there is only one path to take. But why return the 0?
            #The max left and max right subtrees are built recursively up from the bottom/
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            #if the maximum subtree is negative, turn it to 0. Why? Because when total max of a subtree is a negative, that
            #subtree would right away be an invalid subtree to use. If both of them are negative, we wouldn't use either of them
            #*Basically, a parent whose both left and right subtrees are negative would be looked at as a leaf of a potential new path.
            #If only one of those is negative, the negative one is right away not considered
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            """
            Important note: The conditional is used to check whether the TOTAL MAX SUBTREE is negative, not just the value at a node 
            i.e. say you have 3 connected to l=-1 and r=2, we would still choose the path containing the l if the subsequent values
            make the max left subtree >= 2, say l=-1 is connected to a 100. Then the max left subtree is 99. 

            If instead the max subtree on the left was just -1, we would set it to 0, and pick the greater subtree (max=0 vs max=2), so
            obviously we'd choose the one on the right containing the 2.
            """

            #The result will be updated at the parent of the two greatest subtrees
            res[0] = max(res[0], root.val + leftMax + rightMax)

            #the line below is the most important noe here:
            #For each parent, only one of the two subtrees is considered the bigger one. A path can never
            #split into two besides a single point (cur parent).
            #So, for each node, we have to return the value of its greatest subtree (either left or right)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]