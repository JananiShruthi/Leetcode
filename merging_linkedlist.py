# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        i = 0
        temp = list1
        for _ in range(a - 1)                 :
            temp = temp.next

        temp1 = temp.next
        temp.next = list2
        temp2 = list2
        while temp2.next != None:
            temp2 = temp2.next

        for _ in range(b-a+1):
            temp1 = temp1.next

        temp2.next = temp1

        return list1
        



        
            

        
