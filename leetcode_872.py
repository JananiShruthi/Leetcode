# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        stack1 = [root1]
        stack2 = [root2]
        node_val1 = []
        node_val2 = []
        while stack1:
            curr_node = stack1.pop()
            if curr_node.left is not None:
                stack1.append(curr_node.left)
            if curr_node.right is not None:
                stack1.append(curr_node.right)
            if (curr_node.left is None) and (curr_node.right is None):
                node_val1.append(curr_node.val)

        print(f"node_val1: {node_val1}")

        while stack2:
            curr_node = stack2.pop()
            if curr_node.left is not None:
                stack2.append(curr_node.left)
            if curr_node.right is not None:
                stack2.append(curr_node.right)
            if (curr_node.left is None) and (curr_node.right is None):
                node_val2.append(curr_node.val)

        print(f"node_val1: {node_val2}")
        return node_val1 == node_val2
