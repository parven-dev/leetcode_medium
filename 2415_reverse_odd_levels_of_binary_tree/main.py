# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def reverseOddLevels(self, root):
    
            
        if root is None:
                return 
            
        queue = [root]
        level = 0
            
        while queue:
            queue_size = len(queue)
            curr_level = []
                
            for _ in range(queue_size): 
                poped_node = queue.pop(0)
                curr_level.append(poped_node)
                    
                if poped_node.left:
                    queue.append(poped_node.left)
                    
                if poped_node.right:
                    queue.append(poped_node.right)

            if level % 2 == 1:
                values = [node.val for node in curr_level]
                values.reverse()
                for i, node in enumerate(curr_level):
                    node.val = values[i]
            level += 1 
            
        return root.val
        


s1 = Solution()


root = TreeNode(2)

root.left = TreeNode(3)
root.left.left = TreeNode(8)
root.left.right = TreeNode(13)

root.right = TreeNode(5)
root.right.left = TreeNode(21)
root.right.right = TreeNode(34)

print(s1.reverseOddLevels(root))

# print(s1.reverseOddLevels(root))

