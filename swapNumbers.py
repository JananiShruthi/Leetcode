'''The problem is a linked list of number will be given and a variable k is given. This k indicates the kth node from the end and the kth node from the beginning must be swapped'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        temp = dummy

        #moving the 'second' to the k-1th element from the last
        for _ in range(k + 1):
            temp = temp.next 

        while temp is not None:
            second = second.next
            temp = temp.next
        
        for _ in range(k):
            first = first.next

        print("[FIRST]", first.val, " [SECOND]", second.val)
        v = first.val
        first.val = second.next.val
        second.next.val = v

        return dummy.next
        
