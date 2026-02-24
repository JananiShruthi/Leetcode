# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def all_paths(self, node, path, paths):
        if node is None:
            return
        path.append(node.val)
        if node.left is None and node.right is None: # if it is a leaf node
            paths.append(path.copy())
        else:
            self.all_paths(node.left, path, paths)
            self.all_paths(node.right, path, paths)

        path.pop()
        return paths

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        path = []
        paths = []
        all_possible_paths = self.all_paths(root, path, paths)
        for p in all_possible_paths:
            for i in range(len(p)):
                ans += p[i] * pow(2, len(p)-1-i)

        return ans

