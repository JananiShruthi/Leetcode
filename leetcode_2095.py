# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        print("Total elements in the linked list is: ", n)
        if n <= 1:
            return None
        middle = n//2

        ptr = head
        i = 0
        while i < middle - 1:
            ptr = ptr.next
            i += 1

        print("Ptr value: ", ptr.val)

        temp1 = ptr.next
        if temp1:
            ptr.next = temp1.next
        else:
            ptr.next = None
        return head
