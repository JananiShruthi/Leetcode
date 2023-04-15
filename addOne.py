class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 0
        out = []
        digits.reverse()
        for i in range(0, len(digits)):
            if(i == 0):
                val = digits[i] + 1 + c
            else:
                val = digits[i] +  c
            out.append(val%10)
            c = val // 10
        if(c != 0):
            out.append(c)
        out.reverse()
        return out
