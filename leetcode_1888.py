# sliding window
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        r = s + s # for the rotating operation

        alt1 = ""
        alt2 = ""

        for i in range(len(r)):
            if i % 2:
                alt1 += "1"
                alt2 += "0"
            else:
                alt1 += "0"
                alt2 += "1"

        diff1 = diff2 = 0
        l = 0
        res = float("inf")

        for r_idx in range(len(r)):

            if r[r_idx] != alt1[r_idx]:
                diff1 += 1
            if r[r_idx] != alt2[r_idx]:
                diff2 += 1

            if r_idx - l + 1 > n:
                if r[l] != alt1[l]:
                    diff1 -= 1
                if r[l] != alt2[l]:
                    diff2 -= 1
                l += 1

            if r_idx - l + 1 == n:
                res = min(res, diff1, diff2)

        return res
