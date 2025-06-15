class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            # Swap if num is negative
            if num < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(num, num * curr_max)
            curr_min = min(num, num * curr_min)

            max_so_far = max(max_so_far, curr_max)

        return max_so_far
