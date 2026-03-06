class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)
        ones = s.count('1')
        if ones == 1:
            return True
        curr_ones = 0
        for i in range(1, n):
            if s[i] == s[i-1] == '1':
                curr_ones += 1
            else:
                break
        if curr_ones + 1 == ones: # all the ones are grouped together
            return True
        else: # some ones are seperated
            return False
