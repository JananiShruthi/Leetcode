class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output = []
        for i, ele in enumerate(nums):
            if i % 2 != 0:
                print(f"Ele is {ele}")
                for freq in range(0, nums[i-1]):
                    output.append(ele)

        print("Output: ", output)
        return output
