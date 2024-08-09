class Solution {
public:

    static bool isMagicSquare(vector<vector<int>>& grid) {
        int r1sum, r2sum, r3sum, c1sum, c2sum, c3sum, d1sum, d2sum;

        r1sum = grid[0][0] + grid[0][1] + grid[0][2];
        r2sum = grid[1][0] + grid[1][1] + grid[1][2];
        r3sum = grid[2][0] + grid[2][1] + grid[2][2];
        c1sum = grid[0][0] + grid[1][0] + grid[2][0];
        c2sum = grid[0][1] + grid[1][1] + grid[2][1];
        c3sum = grid[0][2] + grid[1][2] + grid[2][2];
        d1sum = grid[0][0] + grid[1][1] + grid[2][2];
        d2sum = grid[2][0] + grid[1][1] + grid[0][2];

        if (r1sum == r2sum && r2sum == r3sum && r3sum == c1sum && c1sum == c2sum &&
            c2sum == c3sum && c3sum == d1sum && d1sum == d2sum) {
            // Check for distinct numbers from 1 to 9
            vector<int> check(10, 0);
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    if (grid[i][j] < 1 || grid[i][j] > 9 || check[grid[i][j]] > 0) {
                        return false;
                    }
                    check[grid[i][j]]++;
                }
            }
            return true;
        }
        return false;
    }

    static int numMagicSquaresInside(vector<vector<int>>& grid) {
        int ans = 0;
        int nrows = grid.size();
        int ncols = grid[0].size();

        for (int i = 0; i <= nrows - 3; i++) {
            for (int j = 0; j <= ncols - 3; j++) {
                vector<vector<int>> subMatrix(3, vector<int>(3));
                for (int x = 0; x < 3; x++) {
                    for (int y = 0; y < 3; y++) {
                        subMatrix[x][y] = grid[i + x][j + y];
                    }
                }
                if (isMagicSquare(subMatrix)) {
                    ans++;
                }
            }
        }
        return ans;
    }
};
