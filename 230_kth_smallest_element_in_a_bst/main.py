
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # def __init__(self):
        # self.root = None
    
    # def insert(self, val):
    #     if val is None:
    #         return
    #     if self.root is None:
    #         self.root = TreeNode(val)
    #     else:
    #         self.insert_recursive(self.root, val)
            
    
    # def insert_recursive(self, node, val):
    #     if val < node.val:
    #         if node.left is None:
    #             node.left = TreeNode(val)
    #         else:
    #             self.insert_recursive(node.left, val)
                
    #     else:
    #         if node.right is None:
    #             node.right = TreeNode(val)
    #         else:
    #             self.insert_recursive(node.right , val)
                
                
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        counter = 0
        result = None
        
        def Traversal(root, k):
            nonlocal counter, result
            if not root:
                return None

            Traversal(root.left, k)
            counter+=1
            
            if counter == k:
                result = root.val
                return 

            Traversal(root.right, k)

            
         
        Traversal(root, k)
        return result

        
        
        
        


bst = Solution()

# values = [3,1,4,None,2]

root = TreeNode(3)
root.left = TreeNode(1)
root.left.right = TreeNode(2)

root.right = TreeNode(4)
# for val in values:
#     bst.insert(val)
    
result = bst.kthSmallest(root, k=1)
print(result)
