class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        row_tuples = [tuple(r) for r in grid]
        col_tuples = []
        for j in range(cols):
            s = []
            for i in range(rows):
                s.append(grid[i][j])
            col_tuples.append(tuple(s))

        row_cnt = Counter(row_tuples)
        col_cnt = Counter(col_tuples)

        ans = 0
        for tup, rcount in row_cnt.items():
            ans += rcount * col_cnt.get(tup, 0)

        return ans
