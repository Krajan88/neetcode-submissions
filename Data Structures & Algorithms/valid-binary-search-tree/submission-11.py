class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        
        def dfs(node):
            if node is None:
                return True
            
            if not dfs(node.left):
                return False
            
            if self.prev is not None and node.val <= self.prev:
                return False
            self.prev = node.val
            
            if not dfs(node.right):
                return False
            
            return True
        
        return dfs(root)