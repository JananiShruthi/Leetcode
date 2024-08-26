##################### The following is the postorder traversal using recursion for the N-ary tree #####################

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:

    def __init__(self):
        self.ans = []

    def postorder(self, root: 'Node') -> List[int]:
        if root == None:
            return 
        print("No. of children: ", len(root.children))

        total = len(root.children)
        for i in range(total):
            self.postorder(root.children[i])
        self.ans.append(root.val)

        return self.ans

##################### The following is the postorder traversal of the N-ary tree without recursion #####################
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        stack = [root]
        ans = []

        while stack:
            node = stack.pop()
            ans.append(node.val)
            # Since we are doing postorder (left, right, root),
            # and we are using a stack, we must push children from left to right
            # so that they are processed from right to left.
            stack.extend(node.children)

        # The ans list will have root -> right -> left order,
        # so we need to reverse it to get left -> right -> root.
        return ans[::-1]
