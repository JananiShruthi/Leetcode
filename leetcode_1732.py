class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = 0
        alti = 0
        for g in gain:
            prefix_sum += g
            if prefix_sum > alti:
                alti = prefix_sum

        return alti
