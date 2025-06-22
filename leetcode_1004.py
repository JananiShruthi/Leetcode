class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_count = 0
        max_count = 0
        p1 = 0
        for p2 in range(len(nums)):
            if nums[p2] == 0:
                zero_count += 1
            
            while zero_count > k:
                if nums[p1] == 0:
                    zero_count -= 1
                p1 += 1

            max_count = max(max_count, p2 - p1 + 1)
        return max_count
            
