# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            curr_node = stack.pop()
            if curr_node.val == val:
                return curr_node
            if curr_node.left is not None:
                stack.append(curr_node.left)
            if curr_node.right is not None:
                stack.append(curr_node.right)
        return None
