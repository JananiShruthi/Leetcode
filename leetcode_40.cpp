class Solution {
public:
    void findcombination(vector<int>& candidates, int target, int start, vector<int>& current, vector<vector<int>>& result) {
        if (target == 0) {
            result.push_back(current);
            return;
        }

        for (int i = start; i < candidates.size(); i++) {
            // Skip duplicates
            if (i > start && candidates[i] == candidates[i - 1]) {
                continue;
            }

            // If the current number exceeds the target, break out of the loop
            if (candidates[i] > target) {
                break;
            }

            // Include the current number in the combination
            current.push_back(candidates[i]);

            // Recursively explore further with the remaining target reduced by candidates[i]
            findcombination(candidates, target - candidates[i], i + 1, current, result); // to ensure that no elements are used agin in the result

            // Backtrack by removing the last number added to the combination
            current.pop_back();
        }
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> result;
        vector<int> current; // to hold the elements that are currently being processed

        findcombination(candidates, target, 0, current, result);
        return result;
    }
};
