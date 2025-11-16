# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max_len = 0
        def maxZigZag(node, direction, length):
            nonlocal max_len
            if not node:
                return 
            max_len = max(length, max_len)
            if direction == 'L':
                maxZigZag(node.right, 'R', length + 1)
                maxZigZag(node.left, 'L', 1)
            else:
                maxZigZag(node.right, 'R', 1)
                maxZigZag(node.left, 'L', length + 1)
        
        maxZigZag(root, 'R', 0)
        return max_len
