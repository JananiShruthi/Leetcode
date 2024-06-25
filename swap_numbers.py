'''Swap the nodes in pairs that are adjacent in a linked list. eg: 1) [1,2,3,4] -> [2,1,4,3] 2) [3,2,4,5,6] -> [2,3,5,4,6]'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy

        while dummy.next is not None:
            node1 = dummy.next
            if node1.next is not None:
                dummy.next = node1.next    
            else:
                break
            node2 = dummy.next
            node3 = node2.next if node2.next is not None else None
            node2.next = node1
            node1.next = node3

            dummy = dummy.next.next

        return first.next

            

