'''A critical point in a linked list is defined as either a local maxima or a local minima.
A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.
A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.
Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.
Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between 
any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1]'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        middle = head
        nxt = head.next
        index = 2
        indices = []
        first_critical_ele = -1
        mindist = maxdist = -1
        
        if nxt.next == None: # If the Linked list is of length 2 
            return [-1, -1]
        else:
            while nxt.next != None:
                print("INDEX NOW: ", index)
                middle =  middle.next
                nxt = middle.next
                if middle.val > prev.val and middle.val > nxt.val:
                    indices.append(index)
                elif middle.val < prev.val and middle.val < nxt.val:
                    indices.append(index)

                index += 1
                prev = prev.next
            if len(indices) > 1:
                maxdist = indices[-1] - indices[0]
                differences = [indices[i+1] - indices[i] for i in range(len(indices) - 1)]
                mindist = min(differences)

            return [mindist, maxdist]
