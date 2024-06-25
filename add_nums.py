# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ini = ListNode(0)
        temp = ini
        head = ini
        c = 0
        s = 0
        while l1 is not None or l2 is not None or c != 0:

            if l1 is not None:
                val1 = l1.val
            else:
                val1 = 0

            if l2 is not None:
                val2 = l2.val
            else:
                val2 = 0
            print("[CARRY]", c)
            s = val1 + val2 + c
            num = s % 10
            c = s // 10
            print("[SUM]", s)
            newNode = ListNode(num)
            ini.next = newNode
            ini = ini.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = head.next
        return result

        
