class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones = 0
        zeros = 0
        max_ones = 0
        max_zeros = 0
        n = len(s)
        if n == 1:
            if s == '1':
                return True
            else:
                return False

        for i in range(1, n):
            if s[i] == s[i-1] == '1':
                ones += 1
            elif s[i] == s[i-1] == '0':
                zeros += 1
            else: # continous breakage
                max_ones = max(max_ones, ones)
                max_zeros = max(max_zeros, zeros)
                ones = 0
                zeros = 0

        max_ones = max(max_ones, ones)
        max_zeros = max(max_zeros, zeros)
        print(f"max_ones: {max_ones+1} ans max_zeros: {max_zeros+1}")
        return (max_ones+1) > (max_zeros+1)
