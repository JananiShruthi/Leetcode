class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        n = len(asteroids)
        i = 1
        for i in range(1, n):
            while stack:
                ele = stack[-1]
                if ele > 0 and asteroids[i] < 0: # opposite direction
                    if abs(ele) < abs(asteroids[i]): # top ele mass is small than asteroid[i]
                        _ = stack.pop()
                        continue
                    elif abs(ele) > abs(asteroids[i]):
                        break # move on to the next asteroid
                    else: # both have same mass but different direction
                        _ = stack.pop()
                        break
                else: #same direction
                    stack.append(asteroids[i])
                    break
            else:
                stack.append(asteroids[i])

        return stack


                        
                        
