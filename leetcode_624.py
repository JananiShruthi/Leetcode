class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val, max_val = arrays[0][0], arrays[0][-1]
        ans = 0

        for i in range(1, len(arrays)):
            curr_min, curr_max = arrays[i][0], arrays[i][-1]

            # Calculate potential distances
            ans = max(ans, abs(max_val - curr_min), abs(curr_max - min_val))

            # Update global min and max
            min_val = min(min_val, curr_min)
            max_val = max(max_val, curr_max)

        return ans
