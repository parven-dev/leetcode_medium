from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        result = []
        queue = [root]

        
        while queue:
            queue_size = len(queue)
            queue_list  = []
            
            for _ in range(queue_size):
                current_node = queue.pop(0)
                queue_list.append(current_node.val)
                
                if current_node.left:
                    queue.append(current_node.left)
                    
                if current_node.right:
                    queue.append(current_node.right)
                    
            result.append(sum(queue_list))
            
        sorted_tree_list = sorted(result, reverse=True)
        if k >= len(result):
            return -1
        return sorted_tree_list[k-1]

            
    
    
    
# root = [5,8,9,2,1,3,7,4,6]

root = TreeNode(5)
root.left = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(1)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(6)

root.right = TreeNode(9)
root.right.left = TreeNode(3)
root.right.right = TreeNode(7)


k = 2   
s1 = Solution()
result = s1.kthLargestLevelSum(root, k)
print(result)