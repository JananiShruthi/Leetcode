# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root, targetSum):
        node_stack = []
        paths = 0
        all_paths = []
        if root:
            node_stack.append((root, [root.val], targetSum - root.val))
        while node_stack:
            curr, curr_path, tsum = node_stack.pop()
            if curr.left:
                p = curr_path + [curr.left.val]
                node_stack.append((curr.left, p, tsum - curr.left.val))
            if curr.right:
                p = curr_path + [curr.right.val]
                node_stack.append((curr.right, p, tsum - curr.right.val))

            #if not curr.left and not curr.right:
            if tsum == 0:
                paths += 1
                all_paths.append(curr_path)

        return paths

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        nodes = []
        ans = 0
        if root:
            nodes.append(root)
        while nodes:
            n = nodes.pop()
            ans += self.dfs(n, targetSum)
            if n.left:
                nodes.append(n.left)
            if n.right:
                nodes.append(n.right)
        return ans
