# use the inplace operation and the 2 pointer approach to remove the duplicates elements from the list 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
            nums[i] = nums[j] # replacing the duplicates by unique elements
        return i + 1
