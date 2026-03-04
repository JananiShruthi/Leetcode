class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0
        rows = len(mat)
        cols = len(mat[0])
        # now we will keep track of number of 1s in each row and each col
        row_ones = {}
        col_ones = {}
        for i in range(rows):
            row_ones[i] = [] 
            for j in range(cols):
                if mat[i][j] == 1:
                    row_ones[i].append([1,j]) # no of ones and the column val
        print(row_ones)

        for i in range(cols):
            col_ones[i] = []
            for j in range(rows):
                if mat[j][i] == 1:
                    col_ones[i].append([1,j])
        print(col_ones)

        for key,val in row_ones.items():
            if len(val) == 1 and len(col_ones[val[0][1]]) == 1:
                ans += 1

        return ans
