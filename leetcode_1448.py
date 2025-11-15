class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_node = 0

        def dfs(node, max_good):
            nonlocal good_node
            if not node:
                return
            
            # Check if this node is good
            if node.val >= max_good:
                good_node += 1
                max_good = node.val

            dfs(node.left, max_good)
            dfs(node.right, max_good)

        dfs(root, root.val)
        return good_node
