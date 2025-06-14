class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != "*":
                stack.append(ch)
            elif ch == "*":
                _ = stack.pop()
        ans = ''.join(stack)
        print(stack)
        return ans
