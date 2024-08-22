class Solution:
    def findComplement(self, num: int) -> int:
        binary = []
        ans = 0
        while num >= 1:
            if(num%2 == 0):
                binary.append(1)
            else:
                binary.append(0)
            num = num // 2
            #binary.append(num % 2)
            #num = num // 2

        print("Complement of binary: ", binary)
        for index, val in enumerate(binary):
            ans += val * math.pow(2, index)

        print("Answer: ", int(ans))
        return int(ans)
        
