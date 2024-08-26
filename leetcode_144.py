# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        
        while root or stack:
            while root: # traverse till the leftmost node
                stack.append(root)
                res.append(root.val)
                root = root.left
            root = stack.pop() # Backtrack and pop the most recent parent node
            print("Root val: ", root.val)
            root = root.right

        return res
        
