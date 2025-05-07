# class TreeNode:

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sum_of_nodes = 0
        
        def traverse(root):
            nonlocal sum_of_nodes
            if not root:
                return None
            
            traverse(root.right)
            sum_of_nodes+=root.val
            root.val = sum_of_nodes
            traverse(root.left)

        traverse(root)
        return root
        

s1 = Solution()
# root = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]

root = TreeNode(4)
root.left = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)

root.left.right.right = TreeNode(3)


root.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)
# s1.bstToGst(s1.bstToGst(root))
print(s1.bstToGst(root))