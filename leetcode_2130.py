# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        i = 0
        index_dict = {0:[head]}
        temp = head

        while temp.next:
            temp = temp.next
            n += 1
            index_dict[n] = [temp]

        print(f"No of nodes: {n}")
        for key,val in index_dict.items():
            val.append(n-key)

        twinsum = {}
        for key, value in index_dict.items():
            twinsum[key] = value[0].val + index_dict[value[1]][0].val


        return max(twinsum.values())

        
