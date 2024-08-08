class Solution {
public:
    vector<vector<int>> spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        vector<vector<int>> ans;
        int totalCells = rows * cols;
        ans.push_back({rStart, cStart});
        int steps = 0; // Number of steps in current direction
        int direction = 0; // 0: right, 1: down, 2: left, 3: up
        
        // Direction vectors: right, down, left, up
        vector<int> dR = {0, 1, 0, -1};
        vector<int> dC = {1, 0, -1, 0};
        
        while (ans.size() < totalCells) {
            // Increment steps for directions 0 and 2 (right and left)
            if (direction == 0 || direction == 2) steps++;
            
            for (int i = 0; i < steps; i++) {
                rStart += dR[direction];
                cStart += dC[direction];
                
                // Check if the new position is within bounds
                if (rStart >= 0 && rStart < rows && cStart >= 0 && cStart < cols) {
                    ans.push_back({rStart, cStart});
                }
            }
            
            // Change direction
            direction = (direction + 1) % 4;
        }
        
        return ans;
        }
};
