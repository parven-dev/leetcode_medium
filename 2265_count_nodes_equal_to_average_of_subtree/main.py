
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
    
  


arr = [4,8,5,0,1,None,6]
arr_len = len(arr)

tree = TreeNode(None)

root = tree.insert_level_order(arr, None, 0, arr_len)

print(root.val)
print(root.left.val)
print(root.right.val)



