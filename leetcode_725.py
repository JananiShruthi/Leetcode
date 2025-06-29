# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        result= []
        temp = head
        n = 0
        while temp:
            temp = temp.next
            n += 1
        print("no. of nodes in LL: ", n)
        # how many ele are gonna be extra 
        r = n % k
        grp = n//k

        if n < k:
            grp = 1
            r = 0
        print("grp: ", grp, " r:", r)

        temp = head

        ans = []
        while temp:
            if len(ans) < grp:
                ans.append(temp)
                temp = temp.next
            if len(ans) >= grp:
                if r > 0:
                    r -= 1
                    ans.append(temp)
                    temp = temp.next
                    ans[-1].next = None
                    result.append(ans[0])
                    ans = []
                elif r == 0:
                    #temp = temp.next
                    ans[-1].next = None
                    result.append(ans[0])
                    ans = []

            # print("Ans: ", ans)
            # print("Result: ", result)
        
        if n < k:
            for j in range(k-n):
                result.append(None)

        # print("final Result:", result)
        return result

