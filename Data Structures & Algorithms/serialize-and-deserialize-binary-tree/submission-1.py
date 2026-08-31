# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #the result list
        res = []


        def dfs(node):
            #keeping track of every None that the tree points to
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #split the serialized string into a list. Not even necessary really, since you can iterate a string itself
        vals = data.split(",")
        self.index = 0

        print(vals)

        def dfs():
            #The tree is rebuilt as the dfs goes further down
            if vals[self.index] == "N":
                self.index += 1
                return None

            root = TreeNode(int(vals[self.index]))
            self.index += 1
            root.left = dfs()
            root.right = dfs()
            """ 
            Why write it like this well we are traversing the string from left ot right and we know that once we are at a n that that current node is none so the previous node is pointing to a none either from a left or rigth side. To choose which side points to the none it was just done recursively by placing root.left = dfs() and root.right = dfs() as long as we dont hit a none a tree is built normally now once we hit a none from the left, we return none and now we build the right side of that node if that part also hits none, we return none for that, SO the parent node went thorugh both root.left and root.right so recursively, the parent node's left or right now points to that leaf node.


            """

            return root
        
        return dfs()

        
