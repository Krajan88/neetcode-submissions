# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}

        #key:value pair here i) key = value of the node, ii) value = index of the node in inorder
        for i in range(len(inorder)):
            hashmap[inorder[i]] = i

        #pointer to the next *unused* value in the preorder list
        #starts at 0 and advances by 1 everytime a node is consumed
        self.preorder_index = 0


        #l and r are the range of indicies of the *inorder* list that the *current call* is reponsible for (inclusive)
        """
        At first it's dfs(0, len(inorder)-1), then it's gonna keep shrinking for each subtree we visit
        """
        def dfs(l, r):
            #l > r represents an empty set for inorder list
            """
            [l,r] where l and r are the indicies of an inorder list. Ex.
            [9,3,15,20,7] at first will have [0,4], then as it shrinks:
            ex. [0,2], there are 3 elements in inorder
                [0,1] there are 2 elements
                [0,0] there is a single leement
                [1,0] an invalid range, this can only occur at the None nodes
            """
            if l > r:
                return None

            #next unconsumed value in preorder is always the root of whatever subtree we're currently building 
            #(guaranteed by preorder's root-first ordering)
            root_val = preorder[self.preorder_index]
            #Iterate through preorder. Once one node/parent was examined we won't have to look back onto it
            self.preorder_index += 1


            #create that new parent using TreeNode()
            root = TreeNode(root_val)               
            #mid is the index of the current parent in the inorder list: 
                #In the inorder list, everything left of mid lies in the left subtree. Everything right of mid lies in the right subtree.
            mid = hashmap[root_val]
                
            #recursively find left and right children for each node. Left is called first to match the preorder traversal order
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            #return root runs at the end of every call that built a node (the ones that didn't build a node return None when l>r)
            return root

        return dfs(0, len(inorder) - 1)
        