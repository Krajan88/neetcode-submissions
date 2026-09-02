# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Solution 2: Find the node you want to delete and in its place return its right child. That way, the parent
will point to the right child of the node want to delete. But first, find the min value in the right subtree
of deletion node, and append the root.left to the left side of that node. 
(basically reattach the del.left to min value of right subtree of root node)

One small negative part about this solution is that the tree could go unevenly deep on the path of
the deleted node.

"""
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        #For the 2 if statements below, root is the parent of the deletion node. We want to update its
        #.right / .left (depending on which one is the deletion node)
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        else:
            #here we are at the deleted node
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left
                
            else:
                cur = root.right

                while cur.left:
                    cur = cur.left
                
                cur.left = root.left

                #Return the right subtree in place of the node we wanna delete, but now the min. value
                #of that right subtree has the whole left subtree of the delteted node attached to it.
                return root.right

        return root
        