class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        return [list(set1 - set2), list(set2 - set1)] ## Set difference operation is being described here...

###############################################################################################


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[], []]
        for val in set(nums1):
            if val not in nums2:
                answer[0].append(val)
        for val in set(nums2):
            if val not in nums1:
                answer[1]q.append(val)
        return answer
        
