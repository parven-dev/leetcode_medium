# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def deepestLeavesSum(self, root) -> int:
        return root
    
    

# root = [1,2,3,4,5,None,6,7,None,None,None,None,8]
root = TreeNode(1)

root.left = TreeNode(2)
root.left.left= TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(7)

root.right = TreeNode(3)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(8)




s1 = Solution()
# print(s1.deepestLeavesSum(root))
print(root.right.right.right.val)
