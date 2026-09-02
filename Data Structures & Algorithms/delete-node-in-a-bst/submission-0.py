# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key > root.val:
            #We assign root.right and root.left here beacuse here, the root represents the parent
            #node of the node we want to delete. And that node that has to be deleted can be either
            #left or right of the parent, so we have to change the .left/.right pointer
            #of said parent
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
                root.val = cur.val
                """
                After updating the node we want to delete with the smallest value in its right subtree, we
                now want to delete that smallest node from the right subtree so that there's no
                repeating values in the bst.
                To do
                """
                root.right = self.deleteNode(root.right, root.val)

        return root
        