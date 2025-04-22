
class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        
    def insert_level_order(self,arr, root, i, n):
        
        if i < n :
            if arr[i] is not None:
                temp = TreeNode(arr[i])
                root = temp
                root.left = self.insert_level_order(arr, root.left, 2 * i + 1, n)
                root.right = self.insert_level_order(arr, root.right, 2 * i + 2, n)
        return root
    
    def averageOfSubtree(self, root) -> int:
        self.counter = 0
     
        def dfs_helper(node):
            if not node:
                return (0, 0)
            
            sum_left, lefts = dfs_helper(node.left)
            sum_right, rights  = dfs_helper(node.right)
            # print(sum_left, lefts, sum_right, rights)
            
            sums = sum_left + sum_right + node.val
            count = lefts + rights + 1
            
            average = sums // count
            
            if average == node.val:
                self.counter +=1
            return (sums, count)
        dfs_helper(root)
        return self.counter
                
            
            
    
    

  


arr = [4,8,5,0,1,None,6]
arr_len = len(arr)

tree = TreeNode(None)

root = tree.insert_level_order(arr, None, 0, arr_len)

print(tree.averageOfSubtree(root))

# print(root.val)
# print(root.left.val)
# print(root.right.val)



