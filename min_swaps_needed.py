'''A swap is defined as taking two distinct positions in an array and swapping the values in them.
A circular array is defined as an array where we consider the first element and the last element to be adjacent.
Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.'''

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        total_ones = sum(nums)
        
        # if all the elements in the list is 0 or all the elements in the list is 1 then there is no need to swap
        if total_ones == 0 or total_ones == n:
            return 0
        
        current_ones = sum(nums[:total_ones])
        max_ones = current_ones
        
        # Use two pointers to slide the window
        for i in range(n):
            current_ones -= nums[i] # removing the first element from the arr
            current_ones += nums[(i + total_ones) % n] # adding the next element (% is to handle the circular nature of the list)
            max_ones = max(max_ones, current_ones)
        
        return total_ones - max_ones # No. of swaps is nothing but the no. of zeros that are avilable in the subarr
