# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        if not root:
                return 0
            
        queue = [root]
        total_operations = 0
            
        while queue:
            queue_len = len(queue)
            queue_level_list = []
            for _ in range(queue_len):
                current_node = queue.pop(0)
                queue_level_list.append(current_node.val)
                
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            if len(queue_level_list) > 1:       
                if sorted(queue_level_list) != queue_level_list:
                    for i in range(len(queue_level_list)):
                        k = i - 1
                        if k >= 0 and queue_level_list[k] > queue_level_list[i]:
                            queue_level_list[k], queue_level_list[i] = queue_level_list[i], queue_level_list[k]
                            total_operations+=1
                        
                        
                
        return total_operations
    
    

root = TreeNode(1)
root.left = TreeNode(4)
root.left.left = TreeNode(7)
root.left.right = TreeNode(6)

root.right = TreeNode(3)
root.right.left = TreeNode(8)
root.right.left.left = TreeNode(9)

root.right.right = TreeNode(5)
root.right.right.right = TreeNode(10)

s1 = Solution()
print(s1.minimumOperations(root))

    #     1
    #    / \
    #   4   3
    #  / \ / \
    # 7  6 8  5
    #       /   \
    #      9    10
