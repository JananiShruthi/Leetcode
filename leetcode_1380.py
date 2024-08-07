class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_row = []
        max_cols = []

        for i in matrix:
            min_row.append(min(i))

        for i in range(len(matrix[0])):
            cols = []
            for j in range(len(matrix)):
                print(f"row = {i} ans col = {j} and ele = {matrix[j][i]}")
                cols.append(matrix[j][i])
            max_cols.append(max(cols))

        print(f"Max cols: {max_cols} and Min cols: {min_row}")

        ans = [val for val in max_cols if val in min_row]
        print(f"FINAL ANSWER: ",ans)
        return ans
