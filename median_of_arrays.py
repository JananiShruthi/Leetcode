class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        print("Merged numbers: ", nums)
        n = len(nums)
        print(n//2)
        if n%2 == 0:
            median = (nums[n//2] + nums[(n//2) - 1])/2
        else:
            median = nums[(n//2)]

        return median
