class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        ps = []
        for i in range(len(speed)):
            ps.append((position[i], speed[i]))

        ps_sorted = sorted(ps, reverse=True)
        # time_taken = {(p,s) : (target - p) / s for p,s in ps}
        # print("time_taken: ", time_taken, "\n")
        for p, s in ps_sorted:
            tt = (target - p) / s
            if not stack:
                stack.append(tt)
            else:
                if tt > stack[-1]: 
                    stack.append(tt)
        print("Stack: ", stack)
        return len(stack)
