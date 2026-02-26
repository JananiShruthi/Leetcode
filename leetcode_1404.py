class Solution:
    def numSteps(self, s: str) -> int:
        num = 0
        steps = 0
        for i in range(len(s)):
            num += int(s[i]) * pow(2, len(s)-1-i)

        print(num)
        while num > 1:
            if num%2 == 0: # if even
                num //= 2
            else: # if odd
                num += 1
            steps += 1

        return steps

