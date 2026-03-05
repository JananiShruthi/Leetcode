class Solution:
    def minOperations(self, s: str) -> int:
        change = 0
        for i in range(len(s)):
            expected = '0' if i % 2 == 0 else '1'
            if s[i] != expected:
                change += 1

        change1 = 0
        for i in range(len(s)):
            expected = '1' if i % 2 == 0 else '0'
            if s[i] != expected:
                change1 += 1

        return min(change, change1)
