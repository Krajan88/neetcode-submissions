# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #inorder values mapped to their indicies
        hashmap = {}

        for i in range(len(inorder)):
            hashmap[inorder[i]] = i

        #l and r are bounds for the subtrees in inorder
        def dfs(preorder, l, r):
            if preorder is None or l > r:
                return None
                
            node_val = preorder.pop(0)

            node = TreeNode(node_val)
            nodeInorder = hashmap[node_val]

            node.left = dfs(preorder, l, nodeInorder-1)
            node.right = dfs(preorder, nodeInorder+1, r)

            return node

        return dfs(preorder, 0, len(inorder)-1)