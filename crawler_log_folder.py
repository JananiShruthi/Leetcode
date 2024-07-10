class Solution:
    def minOperations(self, logs: List[str]) -> int:

        stack = []
        for i in logs:
            if i == "../" and len(stack) != 0: # if stack isn't empty
                stack.pop()
            elif i == "./":
                pass # do nothing - remain in the same folder
            elif i != "./" and i != "../":
                stack.append(i)

        print("[STACK] ",stack)

        return len(stack)
