# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        stack = [(root, 1)]
        min_depth = float('inf')
        while stack:
            curr_node, curr_depth = stack.pop()
            if curr_node.left is None and curr_node.right is None: 
                min_depth = min(min_depth, curr_depth)
            
            if curr_node.left is not None:
                stack.append((curr_node.left, curr_depth+1))
            if curr_node.right is not None:
                stack.append((curr_node.right, curr_depth+1))

        return min_depth
