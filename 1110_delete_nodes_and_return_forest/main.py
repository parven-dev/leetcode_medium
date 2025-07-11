
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: list[int]) -> list[TreeNode]:
        
        my_list = []

        def postOrderTraversal(node):
        
            if node is None:
                return None
            
            node.left = postOrderTraversal(node.left)
            node.right = postOrderTraversal(node.right)
            
            if node.val in to_delete:
                if node.left:
                    my_list.append(node.left) 
                if node.right:
                    my_list.append(node.right)
                    
                return None
            return node
                
            
        if postOrderTraversal(root):
            my_list.append(root)
        return my_list
        
    
    
    

s1 = Solution()

# root = [1,2,3,4,5,6,7]

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)

root.left.right = TreeNode(5)

root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


to_delete = [3,5]

print(s1.delNodes(root, to_delete))