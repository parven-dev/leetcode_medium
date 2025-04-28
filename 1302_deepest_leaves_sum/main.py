# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def deepestLeavesSum(self, root) -> int:
    
        def dfs_level_order_helper(root):
            
            if root is None:
                return 
            
            queue = [root]
            
            while queue:
                queue_size = len(queue)
                curr_level = []
            
                for _ in range(queue_size):
                    poped_node = queue.pop(0)
                    curr_level.append(poped_node.val)
                    
                # print(poped_node.val)

                    if poped_node.left:
                        queue.append(poped_node.left)

                        # my_queue.append(poped_node.left.val)
                    if poped_node.right:
                        queue.append(poped_node.right)
            return curr_level

                        # my_queue.append(poped_node.right.val)
                        
                
        sum_of_deepest_nodes = dfs_level_order_helper(root)
        return sum(sum_of_deepest_nodes)
        
    

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
# print(root.right.right.right.val)
# print(s1.dfs_level_order(root))
print(s1.deepestLeavesSum(root))
