class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                temp = nums[slow]
                nums[slow] = nums[fast]
                nums[fast] = temp
                slow += 1

        print("Nums: ", nums)
