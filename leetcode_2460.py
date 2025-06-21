class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        #nums_temp = nums.copy()
        n = len(nums)
        for i in range(0, n):
            if i < n-1:
                if nums[i] == nums[i+1]:
                    nums[i] = nums[i] * 2
                    nums[i+1] = 0

        nums_temp = nums
        slow = 0
        print("before change: ", nums_temp)
        for fast in range(n):
            if nums_temp[fast] != 0:
                temp = nums_temp[slow]
                nums_temp[slow] = nums_temp[fast]
                nums_temp[fast] = temp
                slow += 1

        print(nums_temp)
        return nums_temp
