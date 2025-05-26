from typing import Optional

class TreeNode:
    def __init__(self,val ):
        self.val = val
        self.left = None
        self.right = None
        
        
class Solution:
    def __init__(self):
        pass
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
            
        self.flatten(root.left)
        self.flatten(root.right)
            
        left_value = root.right
            
        root.right = root.left
        
        root.left = None
        
        current = root
        while current.right:
            current = current.right
        
        current.right = left_value
                