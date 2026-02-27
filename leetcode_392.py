class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = -1
        p2 = 0
        p3 = 0
        while p1 < p2 and p2 < len(t) and p3 < len(s):
            if t[p2] == s[p3]:
                p1 = p2
                p3 += 1
            p2 += 1

        if p3 == len(s):
            return True
        else:
            return False
