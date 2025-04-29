# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def reverseOddLevels(self, root):
        return root
    


s1 = Solution()

# root = [2,3,5,8,13,21,34]

root = TreeNode(2)

root.left = TreeNode(3)
root.left.left = TreeNode(8)
root.left.right = TreeNode(13)

root.right = TreeNode(5)
root.right.left = TreeNode(21)
root.right.right = TreeNode(34)

print(s1.reverseOddLevels(root))

