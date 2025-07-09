from typing import Optional

# If isLefti == 1, then childi is the left child of parenti.
# If isLefti == 0, then childi is the right child of parenti.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> Optional[TreeNode]:
        
        nodes = {}
        children = set()
      
        for parent, child, left_right in descriptions:
          
            if parent not in nodes:
               nodes[parent] = TreeNode(parent)
          
            if child not in nodes:
               nodes[child] = TreeNode(child)
              
          
            if left_right == 1:
               nodes[parent].left = nodes[child]
            else:
               nodes[parent].right = nodes[child]
              
            children.add(child)
          
          
        for value in nodes:
            if value not in children:
                return nodes[value].val
        

        
           
    
    
    
s1 = Solution()
descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
print(s1.createBinaryTree(descriptions))