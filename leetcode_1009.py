class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = []
        ans = 0
        if n == 0:
            return 1
        while n >= 1:
            if n%2 == 0:
                b.append(1)
            else:
                b.append(0)
            n//=2
        print(b)
        for i,bit in enumerate(b):
            ans += bit * pow(2, i)

        print(ans)
        return ans
