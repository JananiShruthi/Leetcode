class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                # 1) collect the string inside [...]
                part = []
                while stack and stack[-1] != '[':
                    part.append(stack.pop())
                stack.pop()  # remove '['

                part.reverse()
                substr = ''.join(part)
                print(substr)

                # 2) collect the number (can be multiple digits)
                num = 0
                base = 1
                while stack and stack[-1].isdigit():
                    num += int(stack.pop()) * base
                    base *= 10

                # 3) push repeated substring back
                stack.append(substr * num)

        return ''.join(stack)
