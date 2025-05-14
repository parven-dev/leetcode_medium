# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.root = None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return
        
        if  p < root.val and  q < root.val :
            return self.lowestCommonAncestor(root.left, p, q)
            
        if p > root.val  and q > root.val :
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root.val
        
    
    
    def insert(self,val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self.insert_recursive(self.root, val)
    
    def insert_recursive(self,node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self.insert_recursive(node.left, val)
                
        else:
            if node.right is None:
                node.right = TreeNode(val)
                
            else:
                self.insert_recursive(node.right, val)
                
                
        
                
    def dfs(self, node):
        if node is None:
            return
        
        
        self.dfs(node.left)
        print(node.val)
        self.dfs(node.right)
                

# root = [6,2,8,0,4,7,9,None,None,3,5]  
root = [6,2,8,0,4,7,9,None,None,3,5]
p = 2
q = 4
bst = Solution()

for val in root:
    if val is not None:
        bst.insert(val)
    
# print(bst.root.val)

# bst.dfs(bst.root)
print(bst.lowestCommonAncestor(bst.root,p, q ))
    