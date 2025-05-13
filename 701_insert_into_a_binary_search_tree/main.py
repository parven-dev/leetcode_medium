
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    
    def insert(self, val):
        self.root = self.insert_recursive(self.root, val)
        
    
    def insert_recursive(self, root, val):
        
        if root is None:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insert_recursive(root.left, val)
        elif val > root.val:
            root.right = self.insert_recursive(root.right, val)
            
        return root
    
    
    def insertIntoBST(self, val: int) -> Optional[TreeNode]:
        self.root = self.insert_recursive(self.root, val )
        
    
    def inorder_traversal(self, node):
        result = []
        if node:
            result.extend(self.inorder_traversal(node.left))
            result.append(node.val)
            result.extend(self.inorder_traversal(node.right))
        return result
    
    def level_order_traversal(self) -> list[int]:
        result = []
        if not self.root:
            return result
        
        queue = deque([self.root])
        
        while queue:
            current_node = queue.popleft()
            result.append(current_node.val)
            
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        
        return result

bst = BinarySearchTree()

# keys = [50, 30, 70, 20, 40, 60, 80]
# keys = [40,20,60,10,30,50,70]
keys = []
val = 5
for key in keys:
    bst.insert(key)

# print(bst.root.val)
bst.insertIntoBST(val)
# print(bst.inorder_traversal(bst.root))
print(bst.level_order_traversal())

