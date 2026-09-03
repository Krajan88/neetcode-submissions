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

        self.preIdx = 0

        #l and r are bounds for the subtrees in inorder
        def dfs(l, r):
            if preorder is None or l > r:
                return None
                
            node_val = preorder[self.preIdx]
            self.preIdx += 1

            node = TreeNode(node_val)
            nodeInorder = hashmap[node_val]

            node.left = dfs(l, nodeInorder-1)
            node.right = dfs(nodeInorder+1, r)

            return node

        return dfs(0, len(inorder)-1)