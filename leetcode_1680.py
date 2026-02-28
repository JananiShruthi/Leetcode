class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7

        ans = 0
        bit_len = 0
        for i in range(1, n + 1):
            if (i & (i - 1)) == 0:
                bit_len += 1

            ans = ((ans << bit_len) + i) % MOD

        return ans


# EXPLANATION
# this is the condition to check if the current number is the power of 2 (2,4,8...)
# we do this becoz only in the powers of 2 the bit length increases (1, 10, 1000...)
# ok now to the part where we calculate the ans:
# 5 -> 101
# 3 -> 11
# so we have to find the decimal(10111),
# so if u see the trick is to push the binary of ans to left 101__ and then add the number it becomes (10111)
