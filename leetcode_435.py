class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x:x[1])
        print(f"sorted_intervals: {sorted_intervals}")
        answer = 0
        end = sorted_intervals[0][1]
        start = sorted_intervals[0][0]
        n = len(sorted_intervals)
        for i in range(1, n):
            if end > sorted_intervals[i][0]: # overlap
                answer += 1
            else:
                end = sorted_intervals[i][1]
        print(answer)
        return answer
