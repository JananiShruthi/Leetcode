class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key = lambda x:x[0])
        start = sorted_intervals[0][0]
        end = sorted_intervals[0][1]
        ans = [[start, end]]
        n = len(sorted_intervals)
        for i in range(1, n):
            if sorted_intervals[i][0] > end: #Non overlap
                ans.append([sorted_intervals[i][0], sorted_intervals[i][1]])
                start = sorted_intervals[i][0]
                end = sorted_intervals[i][1]
            else: #overlap
                val1 = min(start, sorted_intervals[i][0])
                val2 = max(end, sorted_intervals[i][1])
                print(f"{val1} and {val2}")
                ans[-1] = [val1, val2]
                start = val1
                end = val2

        print("Ans: ", ans)
        return ans
