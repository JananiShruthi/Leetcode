# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root:
            queue = deque([root])
        levels = []
        max_level_sum = 0
        max_level = 1
        curr_level = 0
        while queue:
            curr_level += 1
            level = []
            n = len(queue)
            level_sum = 0
            for i in range(n):
                curr_node = queue.popleft()
                level.append(curr_node.val)
                level_sum += curr_node.val
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            levels.append(level)
            if curr_level == 1:
                max_level_sum = level_sum
            if level_sum > max_level_sum:
                max_level_sum = level_sum
                max_level = curr_level
        return max_level
