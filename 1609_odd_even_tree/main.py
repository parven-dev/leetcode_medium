# For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
# For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        queue = [root]
        level = 0
        
        while queue:
            queue_size = len(queue)
            queue_list = []
            
            for _ in range(queue_size):
                current_node = queue.pop(0)
                
                if level % 2 == 0:
                    if current_node.val % 2 == 0:
                        return False
                else:
                    if current_node.val % 2 != 0:
                        return False
                
                queue_list.append(current_node.val)

                    
                if current_node.left:
                    queue.append(current_node.left)
                    
                if current_node.right:
                    queue.append(current_node.right)
            
            
            # if level % 2 == 0:
            #     if queue_list != sorted(queue_list):
            #         return False
            # else:
            #     if queue_list!= sorted(queue_list, reverse=True):
            #         return False
            for i in range(1, len(queue_list)):
                if level % 2 == 0:
                    if queue_list[i] % 2 == 0 or queue_list[i] <= queue_list[i - 1]:
                        return False
                else:
                    if queue_list[i] % 2 != 0 or queue_list[i] >= queue_list[i - 1]:
                        return False

                
            level+=1

        return True
            
    
    
    
root = TreeNode(1)
root.left = TreeNode(10)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(12)
root.left.left.right = TreeNode(8)

root.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.right.right.left = TreeNode(6)
root.right.right.right = TreeNode(2)

s1 = Solution()
result = s1.isEvenOddTree(root)
print(result)
