class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            # Go to the next node pointed to by the current node.
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = nums[0]
        while True:
            if slow == slow2:
                break

            slow = nums[slow]
            slow2 = nums[slow2]

        return slow

'''
This uses "Floyd's Tortoise and Hare algorithm"

Here the trick is to treat the array as a linked list. assume that the elements of the array are not the elements but the position of the next node 
if the array is [3,1,3,4,2] head node is 3 ie, head node is linked with the node in position 3 that is 4. 
similarly for nums[4] it is linked to the element in the position 2. 

so the linked list would be:
3->4->2->3 (head node is linked with node in position 3 (4), now nums[3] ie 4 is linked with node in position 4 ie 2, now nums[2] = 3 cycle

so now we arrived at the cycle. what about where the cycle started. to do this initialize a pts slow2 at the beginning node again. 
now increment slow and slow2 one by one. if they both are the same then that is the meeting point.
'''
