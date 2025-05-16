
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> list[int]:
        
        
        def get_all_element(root1, root2):
            
            result = []
            all_element_of_root1(root1, result)
            all_element_of_root2(root2, result)
            
            return sorted(result)
            
            
        def all_element_of_root1(root1, result):
            if root1 is None:
                return
            
            all_element_of_root1(root1.left, result)
            result.append(root1.val)
            all_element_of_root1(root1.right, result)
            
        def all_element_of_root2(root2, result):
            if root2 is None:
                return 
            
            all_element_of_root2(root2.left, result)
            result.append(root2.val)
            all_element_of_root2(root2.right, result)
        
        return get_all_element(root1, root2)


bst = Solution()

bst.root1 = TreeNode(2)
bst.root1.left = TreeNode(1)
bst.root1.right = TreeNode(4)

bst.root2 = TreeNode(1)
bst.root2.left = TreeNode(0)
bst.root2.right = TreeNode(3)

result = bst.getAllElements(bst.root1, bst.root2)
print(result)




