# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head.next
        s = 0
        result = ListNode(0)
        t1 = result
        while temp != None:
            if temp.val != 0:
                s += temp.val
                temp = temp.next
            elif temp.val == 0:
                #print("[SUM]: ", s)
                node = ListNode(s)  
                t1.next = node
                t1 = t1.next
                s = 0
                temp = temp.next
        return result.next
