# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.hashmap = {}

        for i in range(len(inorder)):
            self.hashmap[inorder[i]] = i

        
        def dfs(preorder, l,r):
            if not preorder or l > r:
                return None

            root_val = preorder[0]
            mid = self.hashmap[preorder[0]]
            
            if mid > r or mid < l:
                return None

            root = TreeNode(preorder.pop(0))

            root.left = dfs(preorder, l ,mid-1)
            root.right = dfs(preorder, mid+1, r)

            return root

        return dfs(preorder, 0, len(preorder)-1)