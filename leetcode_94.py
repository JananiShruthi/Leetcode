# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return 
        self.inorderTraversal(root.left)
        self.ans.append(root.val)
        self.inorderTraversal(root.right)

        return self.ans


################################### The above is the normal recursive solution #############################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []

        while root or stack:
            while root: # traverse till the leftmost node
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
            
        return res

########################### The above is the solution without using recursion but using stack ##################################s
