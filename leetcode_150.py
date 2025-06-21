class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t.startswith('-') and t[1:].isdigit():
                    stack.append(t)
            elif t.isdigit():
                stack.append(t)

            else:
                if len(stack) >= 2:
                    t1 = int(stack.pop())
                    t2 = int(stack.pop())
                    if t == "+":
                        ans =  t1 + t2
                    elif t == "*":
                        ans = t1 * t2
                    elif t == "-":
                        ans = t2 - t1
                    elif t == "/":
                        ans = t2 / t1
                    stack.append(ans)
                else:
                    return int(stack[-1])

            print("Stack: ", stack)
        print("Stack outside loop: ", stack)
        return int(stack[-1])
