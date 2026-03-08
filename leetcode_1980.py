class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        num_bits = len(nums[0])
        n = pow(2,num_bits)
        number = [i for i in range(n)]
        bits_to_nums = []
        for b in nums:
            binary = 0
            for i, bit in enumerate(b):
                binary += int(bit) * pow(2,len(b)-1-i)
            bits_to_nums.append(binary)

        missing = [x for x in number if x not in bits_to_nums]
        num = missing[-1]

        ans = ""
        if num == 0:
            for i in range(num_bits):
                ans += "0"
            return ans
        else:
            while num >= 1:
                ans += str(num%2)
                num = num//2

            ans = ans[::-1]
            for i in range(num_bits - len(ans)):
                ans = "0" + ans
            return ans
