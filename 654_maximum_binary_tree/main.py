# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]):
        stack = []
        for i in range(len(nums)):
            node = TreeNode(nums[i])
            while stack and nums[i] > stack[-1].val:
                node.left = stack.pop()
            
            if stack:
                stack[-1].right = node

            stack.append(node)

        return stack[0]