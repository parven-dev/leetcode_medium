
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        
        if not root:
            return []
        
        result = []
        queue = [root]
        
        
     
        while queue:
            level_size = len(queue)
            level_list = []
            for _ in range(level_size):
                current_node = queue.pop(0)
                level_list.append(current_node.val)

                
                if current_node.left:
                    queue.append(current_node.left)

                if current_node.right:
                    queue.append(current_node.right)

            result.append(level_list)
        return result
            
        
        
        
#  root = [3,9,20,null,null,15,7]    

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
 
s1 = Solution()

result = s1.levelOrder(root)
print(result)
  