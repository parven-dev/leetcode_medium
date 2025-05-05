# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def sumEvenGrandparent(self, root) -> int:
        sums = 0
        
        def dfs(root, parent, grandparent):
            nonlocal sums
            if root is None:
                return 
            
            if grandparent % 2 == 0:
                sums+=root.val
                
            dfs(root.left, root.val, parent)
            dfs(root.right, root.val, parent)
                
                
        dfs(root, 1, 1)
        return sums
    
    
    

root = TreeNode(6)
root.left = TreeNode(7)
root.left.right = TreeNode(7)
root.left.right.left = TreeNode(1)
# root.left.right.right = TreeNode(4)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(9)

root.right = TreeNode(8)
root.right.left = TreeNode(1)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(5)

    
s1 = Solution()
print(s1.sumEvenGrandparent(root))

    


