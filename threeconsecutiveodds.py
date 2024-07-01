class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        for i in range(n):
            if i < n - 2:
                l = arr[i : i + 3]
                if l[0]%2 != 0 and l[1]%2 != 0 and l[2]%2 != 0: #ie if all the consecutive 3 nos are odd
                    return True
        return False


        
